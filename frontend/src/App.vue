<template>
  <div class="page-container">
    <md-app md-mode="reveal">
      <md-app-toolbar class="md-primary">
        <span class="md-title">World of Fib</span>
      </md-app-toolbar>

      <md-app-content>
        <div class="md-layout">
          <md-card class="md-layout-item">
            <app-form
              @update_result="update_result">
            </app-form>
          </md-card>
          <md-card class="md-layout-item">
            <app-result
              :result="result">
            </app-result>
          </md-card>
        </div>
      </md-app-content>
    </md-app>
  </div>
</template>

<script>
import Form from "./components/Form_fib.vue"
import Result from "./components/Result.vue"


export default {
  name: 'app',
  components: {
    "app-form": Form,
    "app-result": Result
  },
  data () {
    return {
      result: ''
    }
  },
  methods: {
    update_result(result) {
      this.result = result;
    }
  }
}
</script>

<style>

</style>
