# -*- coding: utf-8 -*-

fullnamedict = {} #map from main name to full name

with open('packages.txt','rb') as cur_packages_in:
    lines = cur_packages_in.readlines()
    for line in lines:
        line = str(line)
        if line.startswith('PackageFullName'):
            line.strip('\r\n')
            fullname = line[line.find(':')+2:]
            partname = ''
            if fullname.find('_') > 0:
                partname = fullname.split('_')[0]
            else:
                partname = fullname
            print('{0}:  {1}'.format(partname,fullname))
            if partname in fullnamedict:
                fullnamedict[partname].append(fullname)
            else:
                fullnamedict[partname] = [fullname]

need_remove_fullname_list = []

with open('ref_package_name.txt') as ref_pack_name_in:
    lines = ref_pack_name_in.readlines()
    for line in lines:
        if len(line)>len('Microsoft'):
            partname = ''
            if line.find('_') > 0:
                partname = line.split('_')[0]
            else:
                partname = line.strip('\n')
            if partname in fullnamedict:
                for item in fullnamedict[partname]:
                    need_remove_fullname_list.append(item)


with open('remove.bat','w') as bat_out:
    for item in need_remove_fullname_list:
        bat_out.write('powershell -noprofile Remove-AppxPackage {0}\n'.format(item))