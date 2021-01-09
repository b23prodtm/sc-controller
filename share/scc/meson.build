# install GLADE
w = run_command('wrap-files.sh', 'glade', '*.glade')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/glade')
# install GLADE
w = run_command('wrap-files.sh', 'glade/ae', '*.glade')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/glade/ae')

# install PNG
w = run_command('wrap-files.sh', 'images/24x24/status', '*.png')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/icons/hicolor/24x24/status')

# install PNG
w = run_command('wrap-files.sh', 'images/256x256/status', '*.png')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/icons/hicolor/256x256/status')

# install SVG
w = run_command('wrap-files.sh', 'images', ' *.svg')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images')
# install JSON
w = run_command('wrap-files.sh', 'images', ' *.json')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images')

# install SVG
w = run_command('wrap-files.sh', 'images/button-images', '*.svg')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/button-images')

# install SVG
w = run_command('wrap-files.sh', 'images/controller-icons', '*.svg')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/controller-icons')
# install SVG
w = run_command('wrap-files.sh', 'images/controller-images', '*.svg')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/controller-images')

# install SVG
w = run_command('wrap-files.sh', 'images/menu-icons/buttons', '*.svg')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/buttons')
# install PNG
w = run_command('wrap-files.sh', 'images/menu-icons/buttons', '*.png')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/buttons')

# install SVG
w = run_command('wrap-files.sh', 'images/menu-icons/driving', '*.svg')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/driving')
# install PNG
w = run_command('wrap-files.sh', 'images/menu-icons/driving', '*.png')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/driving')

# install PNG
w = run_command('wrap-files.sh', 'images/menu-icons/items', '*.png')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/items')

# install SVG
w = run_command('wrap-files.sh', 'images/menu-icons/media', '*.svg')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/media')
# install PNG
w = run_command('wrap-files.sh', 'images/menu-icons/media', '*.png')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/media')

# install SVG
w = run_command('wrap-files.sh', 'images/menu-icons/system', '*.svg')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/sytem')
# install PNG
w = run_command('wrap-files.sh', 'images/menu-icons/system', '*.png')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/system')

# install PNG
w = run_command('wrap-files.sh', 'images/menu-icons/weapons', '*.png')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/images/menu-icons/weapons')

# install SCCPROFILE
w = run_command('wrap-files.sh', 'default_profiles', '*.sccprofile')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/default_profiles')
# install SCCPROFILE
w = run_command('wrap-files.sh', 'default_profiles', '.*.sccprofile')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/default_profiles')

# install MENU
w = run_command('wrap-files.sh', 'default_menus', '*.menu')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/default_menus')
# install MENU
w = run_command('wrap-files.sh', 'default_menus', '.*.menu')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/default_menus')

# install CSS
w = run_command('wrap-files.sh', 'osd-styles', '*.css')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/osd-styles')
# install JSON
w = run_command('wrap-files.sh', 'osd-styles', '*.json')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc/osd-styles')

# install TEXT
w = run_command('wrap-files.sh', '.', '*.txt')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'share/scc')

# install PIXMAP
install_data(['images/sc-controller.svg'], install_dir: 'share/pixmaps')

# install MIME
install_data(['../../scc-mime-types.xml'], install_dir: 'share/mime/packages')

# install DESKTOP
install_data(['../../scripts/sc-controller.desktop'], install_dir: 'share/application')

# udev RULES
w = run_command('wrap-files.sh', '../../scripts', '*.rules')
sources = w.stdout().strip().split('\n')
install_data(sources, install_dir: 'lib/udev/rules.d')

