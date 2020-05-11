import * as actionsType from '../actions/actionsType';
import {updateObject} from '../utility';

const initialState = {
    token: null,
    loading: false,
    error: null
}

const authStart = (state, action) => {
    return updateObject(state,
        {
            loading: true,
            error: null
        }
    )
}

const authSuccess = (state, action) => {
    return updateObject(state,
        {
            loading: false,
            token: action.token,
        }
    )
}

const authFail = (state, action) => {
    return updateObject(state,
        {
            error: action.error
        }
    )
}

const authLogout = (state, action) => {
    return updateObject(state,
        {
            token: null
        }
    )
}

const reducer = (state = initialState, action) => {
    switch (action.type) {
      case actionsType.AUTH_START:
        return authStart(state, action);
      case actionsType.AUTH_SUCCESS:
        return authSuccess(state, action);
      case actionsType.AUTH_FAIL:
        return authFail(state, action);
      case actionsType.AUTH_LOGOUT:
        return authLogout(state, action);
      default:
        return state;
    }
  };
  
  export default reducer;
