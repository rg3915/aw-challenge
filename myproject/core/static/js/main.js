var app = new Vue({
  el: '#app',
  delimiters: ['${', '}'],
  data: {
    search: '',
    headers: [
      {title: 'id'},
      {title: 'name'},
      {title: 'full_name'},
      {title: 'htm_url'},
      {title: 'stargazers_count'},
    ],
    username: 'rg3915',
    items: []
  },
  methods: {
    getReposJson () {
      axios.get('/repo/json/')
      .then(result => {
        this.items = result.data.data
      })
    },
    getRepos (username) {
      const url = 'https://api.github.com/users/' + username + '/starred'
      axios.get(url)
      .then(result => {
        this.items = result.data
      })
    },
    save
  },
  mounted () {
    this.getReposJson()
  },
  computed: {
    filteredItems () {
      return this.items.filter((item) => {
        return item.description.toLowerCase().indexOf(this.search.toLowerCase())>=0;
      });
    }
  }
});