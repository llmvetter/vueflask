import { createRouter, createWebHistory } from 'vue-router'
import Patient from '../components/Patient.vue'
import Strokecockpit from '../components/Ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Patient",
      component: Patient
    },
    {
      path: '/strokecockpit',
      name: 'Strokecockpit',
      component: Strokecockpit
    },
  ]
})

export default router