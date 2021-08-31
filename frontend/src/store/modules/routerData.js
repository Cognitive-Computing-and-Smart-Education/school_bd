export default {
    state: {
        path: ''
    },
    getters: {
        routerPath(state) {
            return state.path;
        }
    },
    mutations: {
        changeRouterPath(state, payload) {
            state.path = payload;
        }
    },
    actions: {

    }
}
