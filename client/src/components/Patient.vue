<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Patient Dashboard</h1>
          <hr><br><br>
          <button type="button" class="btn btn-success btn-sm" @click="toggleAddBookModal">Add Patient</button>
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

  <!-- add new book modal -->
  <div
    ref="addBookModal"
    class="modal fade"
    :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
    tabindex="-1"
    role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Add a new patient</h5>
          <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleAddBookModal">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="addPatientFullname" class="form-label">Full Name:</label>
              <input
                type="text"
                class="form-control"
                id="addPatientFullname"
                v-model="addPatientForm.full_name"
                placeholder="Enter patient full name">
            </div>
            <div class="mb-3">
              <label for="addPatientStatus" class="form-label">Status:</label>
              <input
                type="text"
                class="form-control"
                id="addBookAuthor"
                v-model="addPatientForm.status"
                placeholder="Enter patient status">
            </div>
            <div class="mb-3">
              <label for="addPatientMoreInfo" class="form-label">More Info:</label>
              <input
                type="text"
                class="form-control"
                id="addPatientMoreInfo"
                v-model="addPatientForm.more_info"
                placeholder="Enter further patient info">
            </div>
            <div class="btn-group" role="group">
              <button
                type="button"
                class="btn btn-primary btn-sm"
                @click="handleAddSubmit">
                Submit
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="handleAddReset">
                Reset
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      activeAddBookModal: false,
      addPatientForm: {
        full_name: '',
        status: '',
        more_info: '',
      },
      patients: [],
    };
  },
  methods: {
    addBook(payload) {
      const path = 'http://localhost:5000/patients';
      axios.post(path, payload)
        .then(() => {
          this.getPatient();
        })
        .catch((error) => {

          console.log(error);
          this.getPatient();
        });
    },
    getPatient() {
      const path = 'http://localhost:5000/patients';
      axios.get(path)
        .then((res) => {
          this.patients = res.data.patients;
        })
        .catch((error) => {

          console.error(error);
        });
    },
    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      this.toggleAddBookModal();
      let read = false;
      if (this.addPatientForm.read[0]) {
        read = true;
      }
      const payload = {
        full_name: this.addPatientForm.full_name,
        status: this.addPatientForm.status,
        more_info: this.addPatientForm.more_info
      };
      this.addPatient(payload);
      this.initForm();
    },
    initForm() {
      this.addPatientForm.full_name = '';
      this.addPatientForm.status = '';
      this.addPatientForm.more_info = '';
    },
    toggleAddBookModal() {
      const body = document.querySelector('body');
      this.activeAddBookModal = !this.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
  },
  created() {
    this.getPatient();
  },
};
</script>