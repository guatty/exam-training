<template>
<a href="http://annales.tutoratcarabienancy.org/">
  <img style="" alt="Logo TCN" src="./assets/logo.png">
  </a>
  <h1>Bon courage pour vos partiels !!</h1>
  <h3>Les sujets ne reprennent que les QCM des Questions Isolées.<br/> Il n'y a plus de QROC ou de zones à pointer aux partiels cette année. <br/>Pour les DP, <a href="https://drive.google.com/drive/folders/1NMteexEN4e6qEag0P8yhex6TLaZ9oOtk">retrouvez-les dans les PDF</a> </h3>
    <router-view v-if="$route.params.id" />
    <div id="listtrainings" v-else>
      <p><u>Appuyez pour commencer l'entraînement désiré :</u> </p>
      <router-link v-for="training in trainings" :key="training.code" :to="{ name: 'trainingsession', params: {id: training.code} }" class="trainingbutton">Tenter l'annale : {{training.name}}</router-link>
    </div>
</template>

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
      url: "http://annales.tutoratcarabienancy.org/availableTrainings",
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
  methods: {
    async dismiss() {
      this.deferredPrompt = null;
    },
    async install() {
      this.deferredPrompt.prompt();
    }
  }
};
</script>


<style>
@font-face {
  font-family: "Noto Color Emoji";
  src: url(https://gitcdn.xyz/repo/googlefonts/noto-emoji/master/fonts/NotoColorEmoji.ttf);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif, "Segoe UI Symbol",
    "Apple Symbols", "Noto Sans Symbols", "Twemoji Mozilla", "Apple Color Emoji",
    "Noto Color Emoji";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #a52990;
  margin: 0 auto;
}

#listtrainings {
  display: flex;
  justify-content: center;
  flex-flow: column nowrap;
  padding: 4em;
  padding-top: 1em;
}
#nav a.router-link-exact-active {
  color: white;
  background: #a01c8e;
}
#nav #normal-nav {
  color: #af1d29;
  background: white;
}

.trainingbutton {
  margin: 0 10px;
  padding: 10px;
  border: none;
  border-radius: 4px;
  font-weight: bolder;
  text-decoration: none;
  padding: 1em;
  border-radius: 4px;
  background-color: #803c27;
  color: cornsilk;
  margin: 1em;
  text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;

}

.buttondrive {
  font-weight: bolder;
}
.buttonadmin {
  font-weight: bolder;
  background-color: orangered;
}

#header {
  display: flex;
  align-items: center;
  justify-content: center;
}
#header h1 {
  font-family: "Roboto", sans-serif;
  display: block;
}
#header img {
  vertical-align: middle;
  height: 9em;
}

@font-face {
  font-family: 'Noto Color Emoji';
  src: url(https://gitcdn.xyz/repo/googlefonts/noto-emoji/master/fonts/NotoColorEmoji.ttf);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif, 'Segoe UI Symbol', 'Apple Symbols', 'Noto Sans Symbols', 'Twemoji Mozilla', 'Apple Color Emoji', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #502c41;
  margin: 0 auto;
}

#nav {
  display: flex;
  justify-content: center;
  flex-flow: row wrap;
}

#bruh {
  display: flex;
  justify-content: space-around;
}


#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 10px;
  border-radius: 4px;
}

#nav a.router-link-exact-active {
  color: white;
  background: #9414a5;
}

#nav a.isactivated {
  color: white;
  background: #9414a5;
}

#nav #normal-nav {
  color: #502c44;
  background: white;
}

button, .buttondrive, .buttonadmin {
  margin: 0 10px;
  padding: 10px;
  border: none;
  border-radius: 4px;
}


#header {
  display: flex;
  align-items: center;
  justify-content: center;
}
#header h1 {
  font-family: "Roboto", sans-serif;
  display: block;
}
#header img {
  vertical-align: middle;
  height: 9em;
}
.ml {
  color: #9414a5;
  font-weight: bold;
}
</style>
