axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'
var app = new Vue({
  el: '#app',
  delimiters: ['${', '}'],
  data: {
    search: '',
    headers: [
      {title: 'id'},
      {title: 'name'},
      {title: 'full_name'},
      {title: 'html_url'},
      {title: 'stargazers_count'},
    ],
    username: 'rg3915',
    items: [
    // {
    //     'slug': 10978967,
    //     'name': 'components-google',
    //     'full_name': 'CollabCodeTech/components-google',
    //     'html_url': 'https://www.github.com/components-google',
    //     'stargazers_count': 3
    //   },
    //   {
    //     'slug': 2686769,
    //     'name': 'boilerplate-manager',
    //     'full_name': 'agencia-tecnologia-palmas/boilerplate-manager',
    //     'html_url': 'https://www.github.com/boilerplate-manager',
    //     'stargazers_count': 16
    //   },
    //   {
    //     'slug': 37907867,
    //     'name': 'coreui-django-boilerplate',
    //     'full_name': 'ni8mr/coreui-django-boilerplate',
    //     'html_url': 'https://www.github.com/coreui-django-boilerplate',
    //     'stargazers_count': 12
    //   },
    ]
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
    saveRepos() {
      let bodyFormData = new FormData()
      // let config = { headers: {'Content-Type': 'multipart/form-data'} }
      bodyFormData.append('item', JSON.stringify(this.items))
      // axios.post('/repo/add/', bodyFormData, config)
      axios.post('/repo/add/', bodyFormData)
      .then(response => {
        this.items = response.data.data
      })
    }
  },
  mounted () {
    this.getReposJson()
  },
  computed: {
    filteredItems () {
      return this.items.filter((item) => {
        return item.name.toLowerCase().indexOf(this.search.toLowerCase())>=0;
      });
    }
  }
});