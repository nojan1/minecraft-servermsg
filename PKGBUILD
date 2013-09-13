# Maintainer: Niklas Hedlund <nojan1989@gmail.com>

pkgname=minecraft-servermsg
pkgver=1.0
pkgrel=1
epoch=1
pkgdesc="Send random messages to minecraft server"
arch=(any)
license=('gpl')
depends=('screen' 'python' 'fortune-mod' 'minecraft-server-multi' 'ln_sensors')
conflicts=()
source=(minecraft-servermsg@.service send-messages.py)

md5sums=('4444c806d632d28a1a7373fb29ae9cf4'
         '6870c7a861a416c78f61433b12ea2d83')

package() {
  install -Dm744 "$srcdir/send-messages.py" "$pkgdir/usr/bin/send-messages.py"
  install -Dm644 "$srcdir/minecraft-servermsg@.service" "$pkgdir/usr/lib/systemd/system/minecraft-servermsg@.service"
}
