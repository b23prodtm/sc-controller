cu_test = declare_dependency(
	include_directories: include_directories('cu_test/'),
	sources: ['cu_test/CuTest.c'],
)

test('test_utils', executable('test_utils',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib],
	sources: [ 'test_utils.c' ]
))

test('test_config', executable('test_config',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, config_lib],
	sources: [ 'test_config.c' ]
))

test('test_param_checker', executable('test_param_checker',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, params_lib, actions_lib, param_checker_lib],
	sources: [ 'test_param_checker.c' ]
))

test('test_parser', executable('test_parser',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, parser_lib],
	sources: [ 'test_parser.c' ]
))

test('test_profile', executable('test_profile',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, parser_lib],
	sources: [ 'test_profile.c' ]
))

test('test_menudata', executable('test_menudata',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, parser_lib],
	sources: [ 'test_menudata.c' ]
))

test('test_modifiers', executable('test_modifiers',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, parser_lib],
	sources: [ 'test_modifiers.c', 'testmapper/testmapper.c' ]
))

test('test_macros', executable('test_macros',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, parser_lib],
	sources: [ 'test_macros.c', 'testmapper/testmapper.c' ]
))

test('test_modeshift', executable('test_modeshift',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, parser_lib],
	sources: [ 'test_modeshift.c', 'testmapper/testmapper.c' ]
))

test('test_actions', executable('test_actions',
	dependencies: [cu_test],
	include_directories: include,
	link_with: [utils_lib, parser_lib],
	sources: [ 'test_actions.c', 'tools.c' ]
))