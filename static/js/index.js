window.app = Vue.createApp({
  el: '#vue',
  mixins: [windowMixin],
  delimiters: ['${', '}'],
  data: function () {
    return {
      games: [],
      players: [],
      nsec: [],
      flutTable: {
        columns: [
          {name: 'id', align: 'left', label: 'ID', field: 'id'},
          {name: 'public_key', align: 'left', label: 'Pubkey', field: 'public_key'},
          {
            name: 'note_id',
            align: 'left',
            label: 'Note ID',
            field: 'note_id'
          },
          {
            name: 'amount',
            align: 'left',
            label: 'Amount',
            field: 'Amount'
          },
          {
            name: 'game',
            align: 'left',
            label: 'Game',
            field: 'game'
          },
          {
            name: 'game_id',
            align: 'left',
            label: 'Game ID',
            field: 'game_id'
          },
          {
            name: 'live',
            align: 'left',
            label: 'Live',
            field: 'live'
          },
          {
            name: 'nip_05',
            align: 'left',
            label: 'NIP05',
            field: 'nip_05'
          }
        ],
        pagination: {
          rowsPerPage: 20
        }
      }
    }
  },
  methods: {
    async getGames() {
      await LNbits.api
        .request(
          'GET',
          '/fluttr/api/v1/games',
          this.g.user.wallets[0].adminkey
        )
        .then(response => {
          this.games = response.data
        })
        .catch(err => {
          LNbits.utils.notifyApiError(err)
        })
    },
    async updateGames() {
      data.wallet = wallet.id
      await LNbits.api
        .request(
          'PUT',
          `/fluttr/api/v1/games`,
          this.g.user.wallets[0].adminkey,
          this.games
        )
        .then(response => {
          this.games = response.data
        })
        .catch(error => {
          LNbits.utils.notifyApiError(error)
        })
    },
    async getNsec() {
      await LNbits.api
        .request(
          'GET',
          '/fluttr/api/v1/nsec',
          this.g.user.wallets[0].adminkey
        )
        .then(response => {
          this.nsec = response.data
        })
        .catch(err => {
          LNbits.utils.notifyApiError(err)
        })
    },
    async updateNsec() {
      data.wallet = wallet.id
      await LNbits.api
        .request(
          'PUT',
          `/fluttr/api/v1/nsec`,
          this.g.user.wallets[0].adminkey,
          this.nsec
        )
        .then(response => {
          this.nsec = response.data
        })
        .catch(error => {
          LNbits.utils.notifyApiError(error)
        })
    },
    async getPlayers() {
      await LNbits.api
        .request(
          'GET',
          '/fluttr/api/v1/players/' + this.nsec.boss,
          this.g.user.wallets[0].adminkey
        )
        .then(response => {
          this.players = response.data
        })
        .catch(err => {
          LNbits.utils.notifyApiError(err)
        })
    },
    async exportCSV() {
      await LNbits.utils.exportCSV(this.flutTable.columns, this.flut)
    }
  },
  async created() {
    await this.getGames()
    await this.getPlayers()
  }
})
