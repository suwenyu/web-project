<template>
  <div>
    <b-form @submit="onSubmit" v-if="show" @submit.stop.prevent>
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your UserName:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.username"
          required
          placeholder="Enter user name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Your First Name:" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="form.first_name"
          required
          placeholder="Enter first name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-4" label="Your Last Name:" label-for="input-4">
        <b-form-input
          id="input-4"
          v-model="form.last_name"
          required
          placeholder="Enter last name"
        ></b-form-input>
      </b-form-group>
    
      <b-form-group id="input-group-5" label="Your Password:" label-for="input-5">
        <b-form-input type="password" id="text-password" aria-describedby="password-help-block" v-model="form.password" :state="validation"></b-form-input>

          <b-form-invalid-feedback :state="validation">
            Your password must be 8-20 characters long.
          </b-form-invalid-feedback>
          <b-form-valid-feedback :state="validation">
            Looks Good.
          </b-form-valid-feedback>
      </b-form-group>


      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>

  </div>
</template>

<script>
import axios from 'axios';

const headers = {
  'Content-Type': 'application/json'
};


  export default {
    data() {
      return {
        form: {
          email: '',
          username: '',
          first_name: '',
          last_name: '',
          password: ''
        },
        show: true
      }
    },
    computed: {
      validation() {
        return this.form.password.length >= 8 && this.form.password.length <= 20
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        let userObj = JSON.stringify(this.form);
        console.log(userObj);


        axios.post("http://localhost:8000/users/", userObj, {
                headers: headers
            }
        )
        .then(function (res){
            console.log(res);
        })
        .catch(function (error) {
            console.log(error);
        });

        alert(JSON.stringify(this.form));
      }
    }
  }
</script>