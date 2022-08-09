<script>
import { Http } from "@capacitor-community/http";
export default {
  data() {
    return {
      deferredPrompt: null,
      trainings: [],
    };
  },
  mounted() {
    Http.request({
      method: "POST",
      url: this.$API_URL + "/availableTrainings",
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json",
      },
    })
      .then(({ data }) => {
        this.trainings = data;
      })
      .catch((err) => console.log(err));
  },
  methods: {},
};
</script>

<template>
    <router-view v-if="$route.params.id" />
    <div id="listtrainings" v-else>
      <p><u>Appuyez pour commencer l'entraînement désiré :</u> </p>
      <router-link v-for="training in trainings" :key="training.code" :to="{ name: 'trainingsession', params: {id: training.code} }" class="trainingbutton">Tenter l'annale : {{training.name}}</router-link>
    </div>
</template>

