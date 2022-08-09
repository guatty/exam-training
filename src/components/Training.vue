<script>
import { Http } from "@capacitor-community/http";
import TrainingElement from "../components/TrainingElement.vue";
export default {
  components: {
    TrainingElement,
  },
  data() {
    return {
      training: null,
      note: "??/20",
      dispCorrectionAll: false,
      currentScoring: {},
    };
  },
  mounted() {
    console.log(this.$route.params.id);
    if (this.$route.params.id != null) {
      Http.request({
        method: "POST",
        url: "http://annales.tutoratcarabienancy.org/questionsForTraining",
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json",
        },
        data: { training_code: this.$route.params.id },
      })
    .then(({ data }) => {
      this.training = data;
    })
    .catch((err) => console.log(err));
    }
  },
  methods: {
    toggleCorrectionAll(){
      this.dispCorrectionAll = !this.dispCorrectionAll;
      if(this.dispCorrectionAll){
        this.calcScore();
      }
    },
    registerScore(trainingelt_id, score){
      this.currentScoring[trainingelt_id] = score;
    },
    calcScore() {
      var s = 0;
      var l = this.training.training_elts.length;
      Object.values(this.currentScoring).forEach(function(value) {
        s = s+value;
      });
      var score = s/l;
      this.note = String(parseFloat(score*20).toFixed(2)) + " /20";
    },
  },
};
</script>


<template>
  <div v-if="training">
    <hr style="width: 70%" />
    <div id="training-head">
      <div>
        <span>Votre note : {{note}}</span>
        <button :onclick="calcScore" class="calcScore" v-if="!dispCorrectionAll">Calculer votre note</button>
      </div>
      <span>Vous réalisez l'entraînement : {{ training.name }}</span>
      <button :onclick="toggleCorrectionAll" class="togglecorrectionall" v-if="dispCorrectionAll">Annuler</button>
      <button :onclick="toggleCorrectionAll" class="togglecorrectionall" v-if="!dispCorrectionAll">Afficher votre note et toutes les corrections</button>
    </div>
    <div id="training">
      <TrainingElement
        v-for="trainingelt in training.training_elts"
        :key="trainingelt.id"
        :trainingelt="trainingelt"
        :forceDispCorrection="dispCorrectionAll"
        @scoreChanged="registerScore(trainingelt.id, $event)"
      />
    </div>
  </div>
</template>


<style>
#training {
  display: flex;
  justify-content: center;
  flex-flow: column nowrap;
}
#training-head {
  background-color: #596b38;
  position: sticky;
  top: 0px;
  padding: 0.3em;
  font-weight: bold;
  color: white;
  /* text-shadow: 2px 0 0 #fff, -2px 0 0 #fff, 0 2px 0 #fff, 0 -2px 0 #fff, 1px 1px #fff, -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff; */
  text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
  display: flex;
  flex-direction: row;
  align-content: space-around;
  justify-content: space-around;
  align-items: center;
}
</style>
