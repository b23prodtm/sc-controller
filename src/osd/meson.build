subdir('common')
subdir('menus')
subdir('keyboard')

scc_osd_daemon = executable('scc-osd-daemon',
	include_directories: include,
	link_with: [ tools_lib, utils_lib, osd_menu_lib, osd_keyboard_lib,
					config_lib, client_lib, gio_client_lib ],
	dependencies: [ dependency('gtk+-3.0', version: '>=3.22.0') ],
	sources: [
		'osd-daemon.c',
	],
	install: true,
	install_dir: bins
)

scc_osd_menu = executable('scc-osd-menu',
	include_directories: include,
	link_with: [ tools_lib, utils_lib, osd_menu_lib ],
	dependencies: [ dependency('gtk+-3.0', version: '>=3.22.0') ],
	sources: [
		'osd-menu.c',
	],
	install: true,
	install_dir: bins
)

scc_osd_keyboard = executable('scc-osd-keyboard',
	include_directories: include,
	link_with: [ utils_lib, osd_keyboard_lib ],
	dependencies: [ dependency('gtk+-3.0', version: '>=3.22.0') ],
	sources: [
		'osd-keyboard.c',
	],
	install: true,
	install_dir: bins
)


run_target('scc-osd-menu',
	command: [
		'sh', '../../meson-run.sh', 'src/osd/scc-osd-menu',
		'-f', '../share/scc/default_menus/Default.menu',
		'-t', 'radial',
		'-c', 'LEFT',
		# '-f', '/e/SC Controller/share/scc/default_menus/Default.menu'
	],
	dependencies: [scc_osd_menu])


run_target('scc-osd-daemon',
	command: [
		'sh', '../../meson-run.sh', 'src/osd/scc-osd-daemon',
	],
	dependencies: [scc_osd_daemon])
