#!/usr/bin/python3

import sys
import os
from pyrpm.spec import Spec, replace_macros


def create_git_am_sh(spec, specfn):
	gitshfn = specfn.replace('.spec', '.sh')

	gitshfile = open(gitshfn,'w')
	if gitshfile:
		for patch in spec.patches:
			tmp = 'git am patch/' + patch + '\n'
			gitshfile.writelines(tmp)
		gitshfile.close()
	return


def create_bitbake_include(spec, specfn):
	bbincludefn = specfn.replace('.spec', '-centos.inc')

	bbincludefile = open(bbincludefn,'w')
	if bbincludefile:
		bbincludefile.writelines('CENTOS_PATCHES = \" \\\n')
		
		for patch in spec.patches:
			tmp = '\t file://' + patch + ' \\\n'
			bbincludefile.writelines(tmp)
	
		bbincludefile.writelines('\t\"\n')
		
		bbincludefile.close()


def main():
	args = sys.argv
	
	if 1 >= len(args):
		print('no args.')
		exit()
	
	if os.path.isfile(args[1]) == False:
		print('not find input file.')
		exit()

	specfn = args[1];
	spec = Spec.from_file(specfn)

	create_git_am_sh(spec, specfn)
	create_bitbake_include(spec, specfn)


if __name__ == "__main__":
	main()
