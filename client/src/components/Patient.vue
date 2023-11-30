<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Patient Dashboard</h1>
          <br><br>
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
                    <button type="button" class="btn btn-warning btn-sm" @click="toggleEditBookModal(book)">Update</button>
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
                id="addPatientStatus"
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
  <!-- edit book modal -->
  <div
    ref="editBookModal"
    class="modal fade"
    :class="{ show: activeEditBookModal, 'd-block': activeEditBookModal }"
    tabindex="-1"
    role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Update</h5>
          <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleEditBookModal">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="editPatientName" class="form-label">Full Name:</label>
              <input
                type="text"
                class="form-control"
                id="editPatientName"
                v-model="editPatientForm.full_name"
                placeholder="Enter Patient Full Name">
            </div>
            <div class="mb-3">
              <label for="editPatientStatus" class="form-label">Status:</label>
              <input
                type="text"
                class="form-control"
                id="editBookAuthor"
                v-model="editPatientForm.status"
                placeholder="Enter Status">
            </div>
            <div class="mb-3">
              <label for="editPatientMoreInfo" class="form-label">More Info</label>
              <input
                type="text"
                class="form-control"
                id="editPatientMoreInfo"
                v-model="editPatientForm.more_info"
                placeholder="Enter more Patient Info">
            </div>
            <div class="btn-group" role="group">
              <button
                type="button"
                class="btn btn-primary btn-sm"
                @click="handleEditSubmit">
                Submit
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="handleEditCancel">
                Cancel
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
        id: '',
        full_name: '',
        status: '',
        more_info: '',
      },
      activeEditBookModal: false,
      editPatientForm: {
        id: '',
        full_name: '',
        status: '',
        more_info: '',
      },
      patients: [],
    };
  },
  methods: {
    addPatient(payload) {
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
      this.editPatientForm.id = '';
      this.editPatientForm.full_name = '';
      this.editPatientForm.status = '';
      this.editPatientForm.more_info = '';
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
    toggleEditBookModal(patient) {
      if (patient) {
        this.editPatientForm = patient;
      }
      const body = document.querySelector('body');
      this.activeEditBookModal = !this.activeEditBookModal;
      if (this.activeEditBookModal) {
        body.classList.add('modal-open');
      } else{
        body.classList.remove('modal-open');
      }
    },
    handleEditSubmit() {
      this.toggleEditBookModal(null);
      let read = false;
      if (this.editPatientForm.read) read = true;
      const payload = {
        full_name: this.editPatientForm.full_name,
        status: this.editPatientForm.status,
        more_info: this.editPatientForm.more_info,
      };
      this.updatePatient(payload, this.editPatientForm.id);
    },
    updatePatient(payload, patientID) {
      const path = `http://localhost:5000/patients/${patientID}`;
      axios.put(path, payload)
        .then(() => {
          this.getPatient();
        })
        .catch((error) => {
          console.error(error);
          this.getPatient();
        });
    },
    handleEditCancel() {
      this.toggleEditBookModal(null);
      this.initForm();
      this.getPatient();
    },
  },
  created() {
    this.getPatient();
  },
};
</script>