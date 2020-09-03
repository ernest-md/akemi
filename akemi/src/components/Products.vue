<template>
  <div id="products" class="row p-3">
    <!-- Div Producte -->
    <div v-for="product in products" :key="product.id" class="col-sm-6 col-md-3 d-flex mb-5">
      <div class="card flex-fill shadow" :price="`${product.price}`">
        <img class="card-img-top p-2 responsive" :src="`${product.src}`" />

        <div class="card-body">
          <p class="card-text m-n1">{{ product.name }}</p>
          <a
            href="#"
            class="stretched-link"
            data-toggle="modal"
            :data-target="`#modal${product.id}`"
          ></a>
        </div>
      </div>

      <!-- Modal Producte -->
      <div :id="`modal${product.id}`" class="modal">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header" style="width:100%">
              <button type="button" class="close" data-dismiss="modal">&times;</button>
            </div>

            <div class="modal-body">
              <img class="responsive pr-5 pl-5 pb-3 pt-n2" :src="`${product.src}`" />
              {{ product.name }}
              <br />
              <span id="preu">{{ product.price }}</span> €
            </div>

            <div class="modal-footer">
              <form class="form-inline" action="/action_page.php">
                <input
                  :id="`inp${product.id}`"
                  type="number"
                  v-model="n"
                  class="form-control mb-2 mr-sm-2"
                  placeholder="1"
                />

                <button
                  :id="`btn${product.id}`"
                  v-on:click="buyProduct"
                  class="btn btn-dark"
                  data-dismiss="modal"
                >Comprar</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "products",
  props: {
    products: Array,

    items: {
      type: Number,
      default: 0
    },

    total: {
      type: Number,
      default: 0
    }
  },

  data() {
    return {
      itemsP: 0,
      totalP: 0,
      n: 1,
      num: 1
    };
  },

  methods: {
    // Metode agafa les dades del producte i la quantitat i les envia al Carrito
    buyProduct() {
      // Aconseguir la ID del producte i el preu
      var bid = event.target.getAttribute("id").slice(3);
      console.log(bid);

      var price = parseFloat(this.products[(this.products.id = bid - 1)].price);

      // Agafar el valor del input
      this.num = parseInt(this.n);
      
        // Treure valors negatius
        if (this.num < 0) {
          this.num = 0;
        }

        // Si no hi ha input la compra es només d'un producte
        if (Number.isNaN(this.num)) {
          this.num = 1;
        }

      // Sumar al valor actual del carrito
      this.itemsP += this.num;
      this.totalP += price * this.num;

      // Amb aquesta linea de codi enviem els resultats al main (App.vue)
      this.$emit("toCart", this.itemsP, this.totalP.toFixed(2));
    }
  }
};
</script>

<style scoped></style>