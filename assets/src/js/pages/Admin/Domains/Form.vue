<template>
    <mw-admin-layout>
        <form @submit.prevent="submit">
            <div class="md:flex md:items-center mb-6 mt-4">
                <div class="md:w-1/4">
                    <label class="block text-grey-darker font-bold md:text-right mb-1 md:mb-0 pr-4" for="username">
                        Name*
                    </label>
                </div>
                <div class="md:w-1/2">
                    <input v-model="form.name" class="bg-grey-lighter appearance-none border border-grey-lighter hover:border-blue rounded w-full py-2 px-4 text-grey-darker" name="name" id="name" type="text" placeholder="example.com" required>
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/4">
                    <label class="block text-grey-darker font-bold md:text-right mb-1 md:mb-0 pr-4" for="username">
                        Destination*
                    </label>
                </div>
                <div class="md:w-1/2">
                    <input v-model="form.destination" class="bg-grey-lighter appearance-none border border-grey-lighter hover:border-blue rounded w-full py-2 px-4 text-grey-darker" name="name" id="name" type="text" placeholder="mail.example.com" required>
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/4">
                    <label class="block text-grey-darker font-bold md:text-right mb-1 md:mb-0 pr-4" for="username">
                        Relay type
                    </label>
                </div>
                <div class="md:w-1/2 md:inline-flex">
                    <div class="relative">
                        <select v-model="form.relay_type" class="block appearance-none w-full bg-grey-lighter hover:border-blue border border-grey-lighter text-grey-darker py-2 px-4">
                            <option value="">Select relay type</option>
                            <option value="smtp">Deliver to my email server (SMTP)</option>
                        </select>
                        <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                        </div>
                    </div>
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/4"></div>
                <div class="md:w-1/2">
                    <label class="block text-grey-darker font-bold mb-1 md:mb-0 pr-4" for="username">
                        <input v-model="form.active" class="mr-2" type="checkbox" />
                        <span class="text-sm">This domain is active</span>
                    </label>
                </div>
            </div>
            <div class="md:flex md:items-center mb-6">
                <div class="md:w-1/4">
                    <label class="block text-grey-darker font-bold md:text-right mb-1 md:mb-0 pr-4" for="username">
                        Allowed accounts*
                    </label>
                </div>
                <div class="md:w-1/2">
                    <input v-model="form.allowed_accounts" class="bg-grey-lighter appearance-none border border-grey-lighter hover:border-blue rounded w-full py-2 px-4 text-grey-darker" name="name" id="name" type="number" required min="-1">
                </div>
            </div>
            <div class="flex flex-row-reverse border-t pt-2">
                <button type="submit" class="flex-no-shrink bg-blue hover:bg-blue-dark border-blue hover:border-blue-dark text-sm border-4 text-white py-1 px-2 rounded shadow">
                    Submit
                </button>
                <button v-if="id" @click="destroy" type="button" class="mr-1 flex-no-shrink bg-red hover:bg-red-dark border-red hover:border-red-dark text-sm border-4 text-white py-1 px-2 rounded shadow">
                    Delete
                </button>
            </div>
        </form>
    </mw-admin-layout>
</template>

<script>
import AdminLayout from '../../../components/AdminLayout.vue';
import { mapGetters } from 'vuex';
import router from '../../../routing/router';
import Form from '../../../classes/Form';
export default {
    props: ['id'],
    data: () => {
        return {
            entity: {},
            form: {}
        }
    },
    mounted() {
        if (this.id) {
            this.get();
        }
        else {
            this.form = new Form({
                name: '',
                destination: '',
                relay_type: '',
                active: '',
                allowed_accounts: null
            });
        }
    },
    components: {
        'mw-admin-layout': AdminLayout
    },
    computed: {
        ...mapGetters(['user'])
    },
    methods: {
        get() {
            axios.get('/api/domains/'+this.id+'/').then(response => {
                this.entity = response.data;
                this.form = new Form({
                    id: response.data.id,
                    name: response.data.name,
                    destination: response.data.destination,
                    relay_type: response.data.relay_type,
                    active: response.data.active,
                    allowed_accounts: response.data.allowed_accounts,
                });
            })
        },
        submit() {
            if (this.id) {
                this.update();
            }
            else {
                this.add();
            }
        },
        add() {
            this.form.post('/api/domains/').then(data => {
                console.log(data);
                router.push('/admin/domains');
            })
        },
        update() {
            this.form.put('/api/domains/'+this.entity.id+'/').then(data => {
                console.log(data);
                router.push('/admin/domains');
            })
        },
        destroy() {
            this.form.delete('/api/domains/'+this.entity.id+'/').then(data => {
                console.log(data);
                router.push('/admin/users');
            });
        }
    }
}
</script>

<style>

</style>