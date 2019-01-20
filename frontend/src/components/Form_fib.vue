<template>
    <div>
        <form novalidate class="md-layout" @submit.prevent="validate_data">
            <md-card-header>
                <div class="md-title">Getting Fibonacci numbers</div>
            </md-card-header>
            <md-card-content>
                <div class="md-layout md-gutter">
                    <div class="md-layout-item md-small-size-100">
                        <md-field :class="get_validation_class('from')">
                            <label for="from">from</label>
                            <md-input type="number" min=2 id="from" name="from" autocomplete="from" v-model="form_data.from" :disabled="sending" />
                            <span class="md-error" v-if="!$v.form_data.from.required">The from is required</span>
                            <span class="md-error" v-else-if="!$v.form_data.from.between">Number can be 0 - 1000000</span>
                        </md-field>
                    </div>
                    <div class="md-layout-item md-small-size-100">
                        <md-field :class="get_validation_class('to')">
                            <label for="to">to</label>
                            <md-input type="number" :min="minimalNumberForTo" id="to" name="to" autocomplete="to" v-model="form_data.to" :disabled="sending" />
                            <span class="md-error" v-if="!$v.form_data.to.required">The to is required</span>
                            <span class="md-error" v-else-if="!$v.form_data.to.between">Number can be {{ minimalNumberForTo }} - 1000000</span>
                        </md-field>
                    </div>
                </div>
            </md-card-content>
            <md-progress-bar md-mode="indeterminate" v-if="sending" />

            <md-card-actions>
                <md-button type="submit" class="md-primary" :disabled="sending">Get answer</md-button>
            </md-card-actions>
        
            <md-snackbar :md-active.sync="answer_got">Answer have got!</md-snackbar>
        </form>
    </div>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, between } from 'vuelidate/lib/validators'


export default {
    mixins: [validationMixin],
    name: 'form_fib',
    data () {
        return {
            form_data: {
                from: 0,
                to: 1
            },
            sending: false,
            answer_got: false
        }
    },
    computed: {
        minimalNumberForTo() {
            return Number(this.form_data.from) + 1;
        },
    },
    validations: {
        form_data: {
            from: {
                required,
                between: between(0, 1000000)
            },
            to: {
                required,
                between(value) {
                    return between(Number(this.minimalNumberForTo), 1000000)(value);
                }
            }
        }
    },
    sockets: {
        connect: function () {
            console.log('socket connected')
        },
        get_result: function(data) {
            this.update_result(data);
        }
    },
    methods: {
        get_validation_class (fieldName) {
            const field = this.$v.form_data[fieldName]
            if (field) {
                return {
                    'md-invalid': field.$invalid && field.$dirty
                }
            }
        },
        validate_data() {
            this.$v.$touch()
            if (!this.$v.$invalid) {
                this.count_fib();
            }
        },
        count_fib() {
            this.sending = true;
            let data = JSON.parse(JSON.stringify(this.form_data));
            data['from'] = Number(data['from']);
            data['to'] = Number(data['to']);
            this.$socket.emit('calculate_fib', data);
        },
        update_result(result) {
            this.$emit('update_result', result);
            this.sending = false;
            this.answer_got = true;
        }
    }
}
</script>
    
<style>

</style>