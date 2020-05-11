import * as actionsType from 'actionsType';
import axios from 'axios';
import { authLoginUrl } from '../constants';

export const authStart = () => {
    return {
        type: actionsType.AUTH_START
    }
}

export const authSuccess = (token) => {
    return {
        type: actionsType.AUTH_SUCCESS,
        token
    }
}

export const authFail = (error) => {
    return {
        type: actionsType.AUTH_FAIL,
        error
    }
}

export const logout = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('expirationDate')
    return {
        type: actionsType.AUTH_LOGOUT
    }
}

export const checkAuthTimeout = expirationTime => {
    return dispatch => {
      setTimeout(() => {
        dispatch(logout());
      }, expirationTime * 1000);
    };
  };


export const login = (username, password) => {
    return dispatch => {
        dispatch(authStart())
        axios.post(authLoginUrl, {
            username,
            password
        })
        .then(res => {
            const token = res.data.key;
            const expirationDate = new Date(new Date().getTime() + 3600 * 1000)

            localStorage.setItem('token', token);
            localStorage.setItem('expirationDate', expirationDate);

            dispatch(authSuccess(token));
            dispatch(checkAuthTimeout(expirationDate))
        })
        .catch(err => {
            dispatch(authFail(err));
        })
    }
}

export const authSignup = (username, email, password1, password2) => {
    return dispatch => {
      dispatch(authStart());
      axios
        .post("http://127.0.0.1:8000/rest-auth/registration/", {
          username: username,
          email: email,
          password1: password1,
          password2: password2
        })
        .then(res => {
          const token = res.data.key;
          const expirationDate = new Date(new Date().getTime() + 3600 * 1000);
          localStorage.setItem("token", token);
          localStorage.setItem("expirationDate", expirationDate);
          dispatch(authSuccess(token));
          dispatch(checkAuthTimeout(3600));
        })
        .catch(err => {
          dispatch(authFail(err));
        });
    };
};

export const authCheckState = () => {
    return dispatch => {
      const token = localStorage.getItem("token");
      if (token === undefined) {
        dispatch(logout());
      } else {
        const expirationDate = new Date(localStorage.getItem("expirationDate"));
        if (expirationDate <= new Date()) {
          dispatch(logout());
        } else {
          dispatch(authSuccess(token));
          dispatch(
            checkAuthTimeout(
              (expirationDate.getTime() - new Date().getTime()) / 1000
            )
          );
        }
      }
    };
};