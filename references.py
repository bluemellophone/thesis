#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, division, print_function


def _replace(line, extras=False):
    replace_dict = {
        # 'jia_caffe:_2014'   : 'jia_caffe_2014',
        'O (1/k2)'          : '{O (1/k2)}',
        'journaltitle'      : 'journal',
        'location'          : 'address',
        '@thesis'           : '@phdthesis',
        '{phdthesis}'       : '{Ph.D. dissertation}',
        '@report'           : '@techreport',
        'issue = {S1}'      : 'number = {{Supplement 001}}',
        'issue = {S12}'     : 'number = {{Special 12}}',
        'Deng'              : '{Deng \\textit{et al.}}',
        'ø'                 : '{\\o}',
        'é'                 : '{\\\'u}',
        'ü'                 : '{\\"u}',
        'Lasagne/Lasagne'   : 'Lasagne/Lasagne [Accessed: 1 Nov. 2015].'
    }

    extras_dict = {
        'Acoustics'          : 'Acoust.',
        'Administration'     : 'Admin,',
        'Administrative'     : 'Administ.',
        'Advances'           : 'Adv.',
        'Advancing'          : 'Adv.',
        'American'           : 'Amer.',
        'Analysis'           : 'Anal.',
        'Annals'             : 'Ann.',
        'Annual'             : 'Annu.',
        'Animal'             : 'Anim.',
        'Apparatus'          : 'App.',
        'Applications'       : 'Applicat.',
        'Applied'            : 'Appl.',
        'Architectural'      : 'Arch.',
        'Association'        : 'Assoc.',
        'Automatic'          : 'Automat.',
        'Biology'            : 'Bio.',
        'Broadcasting'       : 'Broafcast.',
        'Business'           : 'Bus.',
        'Bulletin'           : 'Bull.',
        'Colloquium'         : 'Colloq.',
        'Communications'     : 'Comm.',
        'Communications of'  : 'Comm.',
        'Comm. of'           : 'Comm.',
        'Computer'           : 'Comput.',
        'Computers'          : 'Comput.',
        'Computing'          : 'Comput.',
        'Computer Society'   : 'CS',
        'Conference'         : 'Conf.',
        'Conference of'      : 'Conf.',
        'Conf. of'           : 'Conf.',
        'Conference on'      : 'Conf.',
        'Conf. on'           : 'Conf.',
        'Congress'           : 'Congr.',
        'Convention'         : 'Conv.',
        'Correspondence'     : 'Corresp.',
        'Cybernetics'        : 'Cybern.',
        'Department'         : 'Dept.',
        'Department of'      : 'Dept.',
        'Dept. of'           : 'Dept.',
        'Digest'             : 'Dig.',
        'Ecology'            : 'Ecol.',
        'Economic'           : 'Econ.',
        'Economics'          : 'Econ.',
        'edition'            : 'ed.',
        'editor'             : 'ed.',
        'Education'          : 'Educ.',
        'Electrical'         : 'Elect.',
        'Electronic'         : 'Electron.',
        'Engineering'        : 'Eng.',
        'Ergonomics'         : 'Ergonom.',
        'Evolutionary'       : 'Evol.',
        'Exposition'         : 'Expo',
        'Foundation'         : 'Found.',
        'Geoscience'         : 'Geosci.',
        'Graphics'           : 'Graph.',
        'Government'         : 'Govt.',
        'Industrial'         : 'Ind.',
        'Industry'           : 'Ind.',
        'information'        : 'inform.',
        'Information'        : 'Inform.',
        'Institute'          : 'Inst.',
        'Intelligence'       : 'Intell.',
        'International'      : 'Int.',
        # 'International'      : 'Int\'l',
        'Journal'            : 'J.',
        'Journal of'         : 'J.',
        'J. of'              : 'J.',
        'Laboratory'         : 'Lab',
        'Laboratories'       : 'Labs',
        'Language'           : 'Lang.',
        'Languages'          : 'Lang.',
        'Learning'           : 'Learn.',
        'Letter'             : 'Lett.',
        'Letters'            : 'Lett.',
        'Machine'            : 'Mach.',
        'Magazine'           : 'Mag.',
        'Management'         : 'Manage.',
        'Managing'           : 'Manag.',
        'Mathematic'         : 'Math.',
        'Mathematics'        : 'Math.',
        'Mathematical'       : 'Math.',
        'Mechanical'         : 'Mech.',
        'National'           : 'Nat.',
        'Newsletter'         : 'Newslett.',
        'Nuclear'            : 'Nucl.',
        # 'Neural'             : 'Neur.',
        # 'National'           : 'Nat\'l',
        'Number'             : 'no.',
        'number'             : 'no.',
        'Network'            : 'Netw.',
        'Networks'           : 'Netw.',
        'Occupation'         : 'Occupat.',
        'Organization'       : 'Org.',
        'Philosophical'      : 'Philosph.',
        'Proceedings'        : 'Proc.',
        'Proceedings of'     : 'Proc.',
        'Proc. of'           : 'Proc.',
        'Proceedings of the' : 'Proc.',
        'Proc. of the'       : 'Proc.',
        'Processing'         : 'Process.',
        'Production'         : 'Prod.',
        'Productivity'       : 'Productiv.',
        'Program'            : 'Prog.',
        'Programming'        : 'Prog.',
        # 'Quarterly'          : 'Q.',
        # 'Quarterly'          : 'Quart.',
        'Record'             : 'Rec.',
        'Recognition'        : 'Recog.',
        'Reliability'        : 'Rel.',
        'Report'             : 'Rep.',
        'Research'           : 'Res.',
        'Review'             : 'Rev.',
        'Royal'              : 'Roy.',
        'Science'            : 'Sci.',
        'Selected'           : 'Select.',
        'Society'            : 'Soc.',
        'Sociological'       : 'Sociol.',
        'Statistics'         : 'Stat.',
        # 'Statistical'        : 'Stat\'l',
        'Studies'            : 'Stud.',
        'Supplement'         : 'Suppl.',
        'Support'            : 'Sup.',
        'Support for'        : 'Sup.',
        'Sup. for'           : 'Sup.',
        'Symposium'          : 'Symp.',
        'Symposium of'       : 'Symp.',
        'Symp. of'           : 'Symp.',
        'Symposium on'       : 'Symp.',
        'Symp. on'           : 'Symp.',
        'systems'            : 'syst.',
        'Systems'            : 'Syst.',
        'Technical'          : 'Tech.',
        'Technology'         : 'Tech.',
        'Telecommunication'  : 'Telecommun.',
        'Transactions'       : 'Trans.',
        'Transactions on'    : 'Trans.',
        'Trans. on'          : 'Trans.',
        'University'         : 'Univ.',
        'Vehicular'          : 'Veh.',
        'Vision'             : 'Vis.',
        'Volume'             : 'vol.',
        'volume'             : 'vol.',
        'Working'            : 'Work.',
        # 'Workshop'           : 'Work.',
        'Workshop of'        : 'Workshop',
        'Workshop on'        : 'Workshop',
    }

    if extras:
        replace_dict.update(extras_dict)

    for search, replace_ in replace_dict.iteritems():
        line = line.replace(search, replace_)

    # Fix
    line = line.replace('{BioSci.}', '{BioScience}')
    return line


new_line_list = []
with open('references.raw.bib', 'r') as refs:
    line_list = refs.readlines()
    inside = False
    for line in line_list:
        line = line.strip('\n')

        # inside flag
        if '@' in line and '@string' not in line:
            inside = True
            print(line)
            article = '@article' in line
            inproceedings = '@inproceedings' in line
            incollection = '@incollection' in line
            thesis = '@thesis' in line
            software = '@software' in line
        if inside and line.strip() == '}':
            inside = False
            article = False
            inproceedings = False
            incollection = False
            thesis = False
            software = False

        # remove bad tags
        tag_list = [
            'urldate',
            'file',
            'note',
            'abstract',
            'keywords',
            'eventtitle',
            'shorttitle',
            'shortjournal',
            'issn',
            'isbn',
        ]

        if inside and not software:
            tag_list.append('url')

        flagged_list = [ '%s = ' % (tag, ) in line for tag in tag_list ]
        if True in flagged_list:
            continue

        tag_list = [
            'booktitle',
            'journaltitle',
            'institution',
        ]
        flagged_list = [ '%s = ' % (tag, ) in line for tag in tag_list ]
        extras = True in flagged_list and (article or inproceedings or thesis)

        if inside and thesis:
            line = line.replace('institution = ', 'school = ')

        if inside and incollection:
            line = line.replace('edition = ', 'chapter = ')

        # perform replacements
        line = _replace(line, extras=extras)

        if 'date = ' in line:
            line_ = line.strip().split()
            date = line_[-1]
            date = date.strip(',').strip('{').strip('}').split('-')
            year = int(date[0])
            new_line_list.append('    year = {%s},' % (year, ))
            if len(date) > 1:
                month_dict = {
                    1  : 'Jan.',
                    2  : 'Feb.',
                    3  : 'Mar.',
                    4  : 'Apr.',
                    5  : 'May',
                    6  : 'Jun.',
                    7  : 'Jul.',
                    8  : 'Aug.',
                    9  : 'Sep.',
                    10 : 'Oct.',
                    11 : 'Nov.',
                    12 : 'Dec.',
                }
                month = int(date[1])
                month_str = month_dict[month]
                new_line_list.append('    month = {%s},' % (month_str, ))
            continue

        if 'title = ' in line:
            line_ = line.strip().split(' = ')
            type_ = line_[0]
            content = line_[-1]
            content_list = content.strip(',')[1:-1].split(' ')
            content_list = [
                '{%s}' % c if c.strip('(')[0].isupper() and not c.startswith('{') else c
                for c in content_list
            ]
            content = ' '.join(content_list)
            line = '    %s = {%s},' % (type_, content, )

        # print status
        # if inside:
        #     line_ = line.strip()
        #     if 'title = ' in line and 'journaltitle = ' not in line and 'booktitle = ' not in line:
        #         print(line_)
        #     else:
        #         tag_list = [
        #             'date',
        #         ]
        #         flagged_list = [ '%s = ' % (tag, ) in line for tag in tag_list ]
        #         if True in flagged_list:
        #             print('\t%s' % (line_, ))

        # add new line
        new_line_list.append(line)

with open('references.bib', 'w') as refs:
    content = '\n'.join(new_line_list)
    refs.write(content)
