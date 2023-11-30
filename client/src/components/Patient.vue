<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Patient Dashboard</h1>
          <hr><br><br>
          <button type="button" class="btn btn-success btn-sm">Add Patient</button>
          <br><br>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Full Name</th>
                <th scope="col">Status</th>
                <th scope="col">More information</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(patient, index) in patients" :key="index">
                <td>{{ patient.full_name }}</td>
                <td>{{ patient.status }}</td>
                <td>{{ patient.more_info }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-warning btn-sm">Update</button>
                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        patients: [],
      };
    },
    methods: {
      getPatients() {
        const path = 'http://localhost:5000/patients';
        axios.get(path)
          .then((res) => {
            this.patients = res.data.patients;
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
    created() {
      this.getPatients();
    },
  };
  </script>