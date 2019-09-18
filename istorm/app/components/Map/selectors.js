import { createSelector } from 'reselect';
import { initialState } from 'containers/App/reducer';

/**
 * Direct selector to the mapPage state domain
 */

const selectPopUp = state => state.popup || initialState.popup;

/**
 * Other specific selectors
 */

/**
 * Default selector used by MapPage
 */

const makeSelectPopup = () =>
  createSelector(
    selectPopUp,
    substate => substate,
  );

/* const makeSelectDrawerOpen = () =>
  createSelector(
    selectSidebarDomain,
    substate => substate.drawer.open,
  ); */

export default makeSelectPopup;
export { selectPopUp };
