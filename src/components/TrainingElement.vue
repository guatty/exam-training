<script>
import PropQCM from "../components/PropQCM.vue";
export default {
  components: {
    PropQCM,
  },
  props: {
    trainingelt: Object,
    forceDispCorrection: Boolean,
  },
  computed: {
    shouldDispCorrection() {
      return this.forceDispCorrection || this.dispCorrection;
    },
  },
  data() {
    return {
      dispCorrection: false,
      currentScoring: {},
      currentScore: 0.0,
    };
  },
  created() {},
  methods: {
    toggleCorrection() {
      this.dispCorrection = !this.dispCorrection;
    },
    registerScore(qcm_id, isCorrect){
      this.currentScoring[qcm_id] = isCorrect;
      this.updateCurrentScore();
    },
    updateCurrentScore() {
      var s = 0;
      var l = this.trainingelt.propositions.length;
      Object.values(this.currentScoring).forEach(function(value) {
        if(value){
          s++;
        }
      });
      if(s==l){
        this.currentScore = 1.0;
      }
      else if(s==l-1){
        this.currentScore = 0.5;
      }
      else if(s==l-2){
        this.currentScore = 0.2;
      }
      else{
        this.currentScore = 0.0;
      }
      this.$emit('scoreChanged', this.currentScore);
    },
  },
};
</script>


<template>
  <div class="trainingelt">
    <div class="enonce">
      <div class="item-enonce intit">Enoncé</div>
      <div class="item-enonce item-enonce-center" v-html="trainingelt.enonce"></div>
      <template v-if="!forceDispCorrection">
        <button :onclick="toggleCorrection" class="item-enonce togglecorrection" v-if="!dispCorrection">Corriger ce QCM</button>
        <button :onclick="toggleCorrection" class="item-enonce togglecorrection" v-else>Cacher la correction de ce QCM</button>
      </template>
      <div class="item-enonce" style="white-space: nowrap;" v-if="shouldDispCorrection">Note : {{currentScore}}/1</div>
    </div>
    <PropQCM
      v-for="prop in trainingelt.propositions"
      :key="prop.id"
      :prop="prop"
      :dispCorrection="shouldDispCorrection"
      @inputChanged="registerScore(prop.id, $event)"
    />
  </div>
</template>


<style>
.trainingelt {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 1.5em;
  padding: 2em;
  border-style: double;
  border-color: #596b38;
  border-width: 1em;
  background-color: #803c27;
}
.enonce {
  font-weight: bolder;
  background-color: #989898;
  padding: 1em;
    display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: stretch;
}
.togglecorrection {
  background-color: #90ee90;
  color: white;
  text-shadow: -1px 0 #000,0 1px #000,1px 0 #000,0 -1px #000;
  min-width: 15%;
}
.item-enonce {
  display: flex;
  flex-direction: column;
  justify-content: center;
  vertical-align: middle;
}

.item-enonce-center {
  flex-grow: 1;
  padding-block: 5px;
}

@media screen and (max-width: 600px) {
  .trainingelt {
    margin: 0em;
    padding: 0em;
    padding-block: 2em;
    border-width: 0em;
  }
  .enonce {
    padding: 0em;
    padding-block: 0.5em;
  }
  .togglecorrection {
    text-shadow: -1px 0 #000,0 1px #000,1px 0 #000,0 -1px #000;
  }
  .intit {
    display:none;
  }
}
</style>
