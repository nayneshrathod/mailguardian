<template>
    <div class="sm:container mx-auto sm:px-2 pt-2 pb-8">
        <div class="bg-white border sm:rounded shadow p-2">
            <h2 class="font-normal text-center mb-2">Relay management</h2>
            <p>Here you can manage the hosts, which are allowed to send mail through your deployed node(s)</p>
            <div class="bg-white border sm:rounded shadow table-wrapper">
                <table class="table text-sm">
                    <thead>
                        <tr>
                            <th>IP Address</th>
                            <th>Active</th>
                            <th>Comment</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-if="count == 0">
                            <td colspan="6">There are currently no SMTP relays to display</td>
                        </tr>
                        <tr v-for="item in smtp_relays" :key="item.id" v-else @click="edit(item.id)">
                            <td>{{ item.ip_address }}</td>
                            <td>
                                <div class="items-center text-white leading-none lg:rounded-full flex lg:inline-flex">
                                    <span class="flex rounded-full uppercase px-2 py-1 text-xs font-bold" :class="{ 'bg-green': item.active, 'bg-red': !item.active }" >
                                        {{ item.active | yesno }}
                                    </span>
                                </div>
                            </td>
                            <td>{{ item.comment }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="inline-flex pt-2 rounded" v-if="page_count > 1">
                <button @click="previous" class="bg-grey-light hover:bg-grey text-grey-darkest py-2 px-4 rounded-l" :class="{'select-none cursor-not-allowed bg-grey-lightest hover:bg-grey-lightest' : current == 1}">
                    Prev
                </button>
                <button @click="next" class="bg-grey-light hover:bg-grey text-grey-darkest py-2 px-4 rounded-r" :class="{'select-none cursor-not-allowed bg-grey-lightest hover:bg-grey-lightest' : current == page_count}">
                    Next
                </button>
            </div>
            <div class="mt-4 mb-2">
                <router-link to="/admin/smtp-relays/add" class="flex-no-shrink bg-blue hover:bg-blue-dark border-blue hover:border-blue-dark text-sm border-4 text-white py-1 px-2 rounded shadow no-underline">
                    Add Relay
                </router-link>
            </div>
        </div>
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
import router from '../../../routing/router';
export default {
    data: () => {
        return {
            smtp_relays: [],
            count: 0,
            search: null,
            current: 1,
            page_count: 1
        }
    },
    mounted() {
        this.get();
    },
    computed: {
        ...mapGetters(['user'])
    },
    methods: {
        get(query = null, page = null) {
            let qs = '';
            if (query) {
                qs = '?search='+query;
            }
            if (page) {
                qs = '?page='+page;
            }
            if (query && page) {
                qs = '?search='+query+'&page='+page;
            }
            axios.get('/api/smtp-relays/'+qs).then(response => {
                this.smtp_relays = response.data.results;
                this.count = response.data.count;
                this.current = response.data.current;
                this.page_count = response.data.page_count;
            });
        },
        moment(str) {
            return window.moment(str);
        },
        next() {
            page = this.smtp_relays.next.split("?page=")[1];
            this.get(this.search, page);
        },
        previous() {
            page = this.smtp_relays.previous.split("?page=")[1];
            this.get(this.search, page);
        },
        edit(id) {
            router.push('/admin/smtp-relays/'+id);
        }
    }
}
</script>