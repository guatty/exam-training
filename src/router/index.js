import {
  createRouter,
  createWebHistory
} from 'vue-router'
import SubsiteTraining from '../views/SubsiteTraining.vue'
import Training from '../components/Training.vue'

const routes = [
  { 
    path: '/:id', 
    component: Training,
    name: 'trainingsessionhome'
  }
  , {
    path: '/entrainement/',
    component: SubsiteTraining,
    name: 'training',
    children: [
      { 
        path: '/entrainement/:id', 
        component: Training,
        name: 'trainingsession'
      }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router