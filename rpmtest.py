#!/usr/bin/python3

import sys
import os
from pyrpm.spec import Spec, replace_macros

args = sys.argv

if 1 >= len(args):
	print('no args.')
	exit()

if os.path.isfile(args[1]) == False:
	print('not find input file.')
	exit()

specfn = args[1];
summaryfn = specfn.replace('.spec', '.log');
gitshfn = specfn.replace('.spec', '.sh');
bbincludefn = specfn.replace('.spec', '-centos.inc');

spec = Spec.from_file(specfn)

gitshfile = open(gitshfn,'w')
if gitshfile:
	for patch in spec.patches:
		tmp = 'git am patch/' + patch + '\n'
		gitshfile.writelines(tmp)
	gitshfile.close()


bbincludefile = open(bbincludefn,'w')
if bbincludefile:
	bbincludefile.writelines('CENTOS_PATCHES = \" \\\n')
	
	for patch in spec.patches:
		tmp = '\t file://' + patch + ' \\\n'
		bbincludefile.writelines(tmp)

	bbincludefile.writelines('\t\"\n')
	
	bbincludefile.close()

#print(spec.version)

#for source in spec.sources:
#	print(source)
#	print(replace_macros(source, spec))


#for patch in spec.patches:
#	print("git am patch/",patch,sep='')


#print(spec.changelog)

#for package in spec.packages:
#	print(f'{package.name}: {package.summary if hasattr(package, "summary") else spec.summary}')
