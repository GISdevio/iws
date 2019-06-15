/*
 *
 * MapPage reducer
 *
 */
import produce from 'immer';
import { DEFAULT_ACTION } from './constants';

var currentTime = new Date();
currentTime.setUTCHours(0, 0, 0, 0);

export const initialState = {
  options: {
    center: [41.879156, 12.457727],
    zoom: 6,
    timeDimension: true,
    timeDimensionOptions: {
        /* timeInterval: "2019-03-30/2019-04-30",
        period: "PT1H",*/
        currentTime: currentTime.getTime()
    }, 
    timeDimensionControl: true,
    minZoom: 2,
     maxBounds: [
      [-85, -180],
      [85, 180],
    ],
  },
  baseLayers: ["wiki"],
  wmsLayers: [
    /* [{
      url: "http://dev.plasive.org:8085/geoserver/wms",
      isTimeseries: true,
      options: {
        layers: 'remotesensing:ndvi',
        transparent: true,
        format: 'image/png',
        version: "1.3.0",
        tiled: true
      }
    }], */
    [{
      //OTTIMA PAGINA DI ESEMPI SUL THREDDS
      //https://wambachers-osm.website/webcommon/js/leaflet/plugins/Leaflet.TimeDimension/examples/example7.html
      name: "test",
      id: "idDITEST",
      url: "http://thredds.socib.es/thredds/wms/operational_models/oceanographical/hydrodynamics/model_run_aggregation/wmop/wmop_best.ncd",
      isTimeseries: true,
      options: {
        layers: 'salt',
        format: 'image/png',
        transparent: true,
        abovemaxcolor: "extend",
        belowmincolor: "extend",
        numcolorbands: 40,
        styles: 'boxfill/mpl_rdbu_r'
      }
    }]
]
};

/* eslint-disable default-case, no-param-reassign */
const mapPageReducer = (state = initialState, action) =>
  produce(state, (/* draft */) => {
    switch (action.type) {
      case DEFAULT_ACTION:
        break;
    }
  });

export default mapPageReducer;