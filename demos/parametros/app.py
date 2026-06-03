import web

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()


class Parametros:
    def GET(self):    
        titulo = "Titulo desde python"
        descripcion = """loreLorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non malesuada ligula. Sed in tempus odio. Vestibulum non leo nibh. Suspendisse at dui eleifend, maximus libero at, porta elit. Nunc augue sem, dignissim a elit ac, ultrices consequat magna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec erat quam, lobortis eu venenatis ut, maximus non metus. Duis pellentesque dolor risus, in fringilla diam sagittis vel.
                    Vestibulum vel purus consectetur, mollis ex eu, convallis enim. Phasellus sagittis vel metus nec volutpat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi ac aliquet odio. Ut tempor libero lacus, ac tempus magna maximus nec. Etiam lacinia eros non orci fringilla egestas. Phasellus venenatis eleifend nisl, eget aliquam nisi dignissim eu. Morbi ac nulla urna. Cras egestas ornare nibh, non pretium nisi interdum ut. Vivamus in vestibulum nulla, semper laoreet ligula. Curabitur maximus, magna eget egestas euismod, turpis purus aliquam felis, eget rutrum purus nisl sed risus. Nullam interdum, tellus ut dignissim efficitur, lacus eros iaculis augue, at dapibus sapien justo in ante. Etiam vulputate elit eu tortor fermentum, at sollicitudin dolor semper.
                    Curabitur vitae pellentesque magna. Vivamus sit amet purus at massa blandit rutrum sed vitae sem. Aenean turpis neque, vestibulum at nibh sit amet, aliquam venenatis enim. Pellentesque luctus odio et sem facilisis, id sodales turpis imperdiet. Donec a turpis id arcu porta dignissim. Pellentesque at nulla eu mi efficitur feugiat. Etiam blandit finibus neque, ac fringilla quam viverra non. Aliquam sit amet dui at tellus venenatis sollicitudin id a mauris. Nulla facilisi. Proin nulla enim, suscipit vitae dui volutpat, faucibus dignissim mauris.
                    In suscipit augue vel justo vehicula consectetur. Curabitur sit amet mauris eget ex faucibus mattis. Quisque at tortor non nisl finibus elementum. Nullam scelerisque fermentum nibh, eu sodales urna lacinia in. Curabitur scelerisque nulla at tempor sodales. Curabitur metus arcu, sollicitudin et gravida ultricies, interdum et eros. Ut vel consequat neque, vitae luctus sem. Nunc justo tortor, viverra nec dui at, posuere maximus felis. Etiam tincidunt tristique malesuada. Quisque accumsan ex sed est mollis semper. Donec malesuada nec lacus dignissim placerat. Proin ex dolor, iaculis sed malesuada quis, lobortis id mi. Aliquam erat volutpat. Curabitur nec accumsan mi. Nullam congue eleifend varius. Aenean vel lacinia dolor, nec congue orci.
                    In ac dictum risus, posuere pretium tellus. Sed malesuada ligula in augue tincidunt sodales. Nunc vehicula justo ac cursus tempor. Praesent porta consectetur nunc, sit amet feugiat ante blandit a. Ut tempor laoreet risus a varius. Aenean sed elit vitae nulla consectetur ornare. Nam ullamcorper iaculis metus ut interdum. Sed vitae vestibulum tellus."""
        return render.parametros(titulo, descripcion)

if __name__ == "__main__":
    app.run()
