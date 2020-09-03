<template>
  <div id="app" class="small-container">
    <div id="bg" class="bg-white pl-3 pr-3 pb-1">
      <!-- Encabezado -->
      <div id="r1" class="row p-2">
        <div class="col-sm-5 col-5 mt-3">
          <img id="logo" src="imgs/logo_akemi.png" alt="Logo Akemi" class="responsive" />
        </div>

        <div id="blank" class="col-sm col-1"></div>

        <div class="col-6 d-block d-sm-none float-right">
          <button
            id="dropdown"
            class="btn btn-secondary dropdown-toggle d-block d-sm-none"
            type="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          ></button>
        </div>

        <div class="col-sm-6 d-none d-sm-block" aria-labelledby="dropdown">
          <div class="row">
            <!-- Products / Brands / Akemi Sets -->
            <div id="block1" class="col-sm bg-light mt-n2">
              <ul class="nav flex-column ml-n2 mt-3 mb-2">
                <li class="nav-item m-n2">
                  <a class="nav-link" href="#">Products</a>
                </li>
                <li class="nav-item m-n2">
                  <a class="nav-link" href="#">Brands</a>
                </li>
                <li class="nav-item m-n2">
                  <a class="nav-link" href="#">Akemi Sets</a>
                </li>
              </ul>
            </div>

            <!-- About us / Register / Login -->
            <div id="block2" class="col-sm bg-light mt-n2">
              <ul class="nav flex-column ml-n2 mt-3 mb-2">
                <li class="nav-item m-n2">
                  <a class="nav-link" href="#">About us</a>
                </li>
                <li class="nav-item m-n2">
                  <a class="nav-link" href="#">Register</a>
                </li>
                <li class="nav-item m-n2">
                  <a class="nav-link" href="#">Login</a>
                </li>
              </ul>
            </div>

            <!-- VUE Carrito -->
            <div id="block3" class="col-sm bg-dark mt-n2">
              <carrito :items="items" :total="total" />
            </div>
          </div>
        </div>
      </div>

      <!-- Banner -->
      <div id="banner" class="row mt-3">
        <div class="col-sm shadow p-2 mt-3 mb-2 mr-3 ml-3 bg-white">
          <img src="imgs/banner1.png" alt="Banner" class="responsive" />
        </div>
      </div>

      <!-- New Products -->
      <div class="row p-2">
        <div class="col-sm-6 mt-4">
          <img src="imgs/new_products.png" alt="New Prodcuts" />
        </div>
      </div>

      <!-- VUE Productes : @toCart crida al metode que agafa les dades de les compres -->
      <products :products="products" @toCart="compraItems" :items="items" :total="total" />
    </div>
  </div>
</template>

<script>
import Products from "@/components/Products.vue";
import Carrito from "@/components/Carrito.vue";

export default {
  name: "app",
  components: {
    Products,
    Carrito
  },
  data() {
    return {
      products: [],
      items: 0,
      total: 0
    };
  },

  methods: {
    // Metode per sumar la compra de Producres al Carrito
    compraItems(itemsP, totalP) {
      this.items = itemsP;
      this.total = totalP;
    },

    // Metode per agafar les dades del Servidor FLASK on es troba la base de dades dels productes
    fetchProducts: function() {
      const baseURI = "http://127.0.0.1:5000/akemi/products/";
      this.$http.get(baseURI).then(result => {
        this.products = result.data;
      });
    }
  },

  // Metode que fa que el metode fetchProducts() s'arranqui abans de montar l'aplicació
  beforeMount() {
    this.fetchProducts();
  }
};
</script>

<style scoped></style>
