# -*- coding: utf-8 -*-
import web
import json

render = web.template.render("views/")

urls = (
    "/index(.*)", "index"
)

class index:
    ciudades = []
    data = []
    productos = []
    derivados = {}
    dercity = {}
    
    def GET(self, val):
        val = []
        with open('200datos.json', 'r') as file:
            self.data = json.load(file)
        self.determinate_cities()
        self.determinate_products()
        self.determinate_by_cities()
        val.append(self.derivados)
        val.append(self.dercity)
        return render.index(val)
    
    def determinate_cities(self):
        for row in self.data["results"]:
            if len(self.ciudades) == 0:
                self.ciudades.append(row["estado"])
            else:
                if row["estado"] in self.ciudades:
                    continue
                else:
                    self.ciudades.append(row["estado"])
                    
    def determinate_products(self):        
        for row in self.data["results"]:
            if len(self.productos) == 0:
                self.productos.append(row["producto"])
            else:
                if row["producto"] in self.productos:
                    continue
                else:
                    self.productos.append(row["producto"])
                    
    def calculate_no_stores(self, producto):
        cont = 0
        for row in self.data["results"]:
            if row["producto"] == producto:
                cont += 1
            else:
                continue
        self.derivados[producto] = [cont]
        
    def calculate_no_cities(self, city):
        cont = 0
        for row in self.data["results"]:
            if row["estado"] == city:
                cont += 1
            else:
                continue
        self.dercity[city] = [cont]
                    
    def determinate_by_cities(self):
        for producto in self.productos:
            self.calculate_no_stores(producto)
            
        for city in self.ciudades:
            self.calculate_no_cities(city)
    
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
