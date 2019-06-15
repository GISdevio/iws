/**
 *
 * LoginForm
 *
 */
import iso8601 from 'iso8601-js-period';
window.nezasa = {iso8601: iso8601}

import React from 'react';
import PropTypes from 'prop-types';

import 'leaflet/dist/leaflet.css';
import "leaflet-timedimension/dist/leaflet.timedimension.control.css";
import L from 'leaflet';
L.Icon.Default.imagePath = 'https://npmcdn.com/leaflet@1.0.1/dist/images/';
import "leaflet-timedimension/src/leaflet.timedimension";
import "leaflet-timedimension/src/leaflet.timedimension.util";
import "leaflet-timedimension/src/leaflet.timedimension.control";
import "leaflet-timedimension/src/leaflet.timedimension.layer";
import "leaflet-timedimension/src/leaflet.timedimension.layer.wms";
import "leaflet-timedimension/src/leaflet.timedimension.player";


import { FormattedMessage } from 'react-intl';
import messages from './messages';

import { withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const styles = (theme) => {
  return {
    appBar: {
      zIndex: theme.zIndex.drawer + 1,
    }
  }
};

class Map extends React.Component {
  

  constructor(props) {
    super(props);

    this.state = {
      map: null
    };

  }

  getChildContext() {
    return { map: this.state.map };
  }

  componentDidMount() {
    const options = this.props.options;
    const map = L.map(this.refs.map, options);

    //map.on('moveend', this.handleChange);

    this.setState({ map });
  }

  componentWillUnmount() { 
    this.state.map.remove(); 
  }

  render () {
    return (
      <div ref="map" style={{ height: 'calc(100vh - 64px)', width: '100%', minHeight: '100%' }}>
        { this.state.map ? this.props.children : undefined }
      </div>
    )
  }
}
Map.childContextTypes = {
  map: PropTypes.object
};
export default withStyles(styles, {withTheme: true})(Map);