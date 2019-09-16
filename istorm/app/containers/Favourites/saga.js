import { call, put, select, takeLatest  } from 'redux-saga/effects';
import { REQUEST_FAVOURITES, DELETE_FAVOURITE, POST_FAVOURITE} from 'containers/Favourites/constants';
import { requestFavouritesSuccess, requestError, deleteFavouriteSuccess, /* postFavouriteSuccess */ } from '../../containers/Favourites/actions';
import { favourites, postFavourite, deleteFavourite } from 'utils/api';

export function* FavouritesSaga(action) {
  /* const options = {
    method: 'get'
  }; */
  try {
    const request = yield call(favourites);
    yield put(requestFavouritesSuccess(request));
    
  } catch(e) {
    yield put(requestError(e.message));
    
  }
}

export function* deleteFavouriteSaga(action) {
  const options = {
    method: 'delete'
  }; 
  try {
    const request = yield call(deleteFavourite, action.id);
    yield put(deleteFavouriteSuccess(request));
    yield call(FavouritesSaga)
  } catch(e) {
    yield put(requestError(e.message));

  }
}

export function* postFavouriteSaga(action) {
  const options = {
    method: 'post',
    body: {...action.Params}
  };
  try {
    const request = yield call(postFavourite, options);
    // yield put(postFavouriteSuccess(request));
    yield call(FavouritesSaga)
  } catch(e) {
    yield put(requestError(e.message));

  }
}
 
export default function* favSaga() {
    yield takeLatest(REQUEST_FAVOURITES, FavouritesSaga);
    yield takeLatest(DELETE_FAVOURITE, deleteFavouriteSaga);
    yield takeLatest(POST_FAVOURITE, postFavouriteSaga);
}
