"""
    While doing development, I need to load a single document
    into indivo. This is a simple management command to perform
    that task
"""

import os.path
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from indivo.models import Document
from indivo.models import PHA
from indivo.models import Record
from indivo.models import Principal

class Command(BaseCommand):
    args = ''
    help = """Import one or more objects directly into the indivo database:

There are two usages:

    python manage.py loaddoc --replaces "77fb8862-090b-4242-b7b9-1af353dd4026" [--mimetype=application/xml] newdoc.xml

or 
    python manage.py loaddoc --record=483eeed3-1788-47ee-8782-c8f5a450835f [--mimetype=application/xml] [--creator=allergies@apps.indivo.org] newdoc.xml

"""
    option_list = BaseCommand.option_list + (
        make_option('--pha',
            action='store',
            dest='pha',
            type='string',
            help='An identifier for the application (PHA) that this document belongs to. Only required when an externalid is provided',
        ),
        make_option('--record',
            action='store',
            dest='record',
            type='string',
            help='An identifier for the record that this document will be linked to',
        ),
        make_option('--mimetype',
            action='store',
            dest='mimetype',
            type='string',
            help='The mime-type for the document - defaults to "application/xml" ',
        ),
        make_option('--externalid',
            action='store',
            dest='externalid',
            type='string',
            help='The external id of the document.',
        ),
        make_option('--replaces',
            action='store',
            dest='replaces',
            type='string',
            help='Where this document replaces an existing document, this is the id of the existing document',
        ),
        make_option('--creator',
            action='store',
            dest='creator',
            type='string',
            help='id or email of creator of the document as per ',
        ),
    )
    output_transaction = True

    def handle(self, *args, **options):
        if len(args) == 0:
            raise CommandError('No files listed for import')

        if (options.get('externalid') or options.get('replaces')) and len(args) > 1:
            raise CommandError('Only one file can be specified with the externalid or replaces options')

        for filename in args:
            if not os.path.isfile(filename):
                raise CommandError('Cannot locate file [%s]', filename)

        params = {}

        if options['mimetype']:
            mimetype = params['mime_type'] = options['mimetype']
        else:
            mimetype = params['mime_type'] = 'application/xml'

        if options['replaces']:
            olddoc = Document.objects.filter(pk=options['replaces'])
            if len(olddoc) == 0:
                raise CommandError('Cannot locate document to be replaced [%s]', options['replaces'])
            if options['verbosity'] > 1:
                print "Replacing document: ", filename
            content = open(args[0], 'r').read()
            olddoc.replace(content, mimetype)

        else:
            if options['record']:
                records = Record.objects.filter(id=options['record'])
                if len(records) == 0:
                    records = Record.objects.filter(external_id=options['record'])
                if len(records) == 0:
                    raise CommandError('Cannot locate record [%s], You must provide a record.id or a record.external_id', options['record'])
                assert len(records) == 1
                params['record'] = records[0]
            else:
                raise CommandError('You must provide a record parameters [indivo id or external id] to attach this document to')

            if options['externalid']:
                if not options['pha']:
                    raise CommandError('You can only specify the external_id if you also specify the PHA')

                pha = None
                phas = PHA.objects.filter(name=options['pha'])
                if len(phas) == 0:
                    raise CommandError('Cannot locate pha [%s], I have %s', options['pha'], PHA.objects.all().value_list('name'))
                assert len(phas) == 1
                pha = phas[0]
                params['external_id'] = Document.prepare_external_id(options['externalid'], pha)

            if options['creator']:
                creators = Principal.objects.filter(id=options['creator'])
                if len(creators) == 0:
                    creators = Principal.objects.filter(email=options['creator'])
                if len(creators) == 0:
                    raise CommandError('The creator you provided cannot be located in the principals table using the id or email')
                assert len(records) == 1
                params['creator'] = creators[0]

        count = 0
        for filename in args:
            if options['verbosity'] > 1:
                print "Loading document: ", filename
            params['content'] = open(filename, 'r').read()
            Document.objects.create(**params)
            count += 1
        if options['verbosity'] > 1:
            print count, "documents loaded ", filename
