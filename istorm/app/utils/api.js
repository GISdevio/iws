import request from "./request";

const BASE_URL = process.env.API_URL;
const defaultOption = {
    headers: new Headers({
        'Accept': 'application/json', 
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
      }),
};

const getOption = (option) => {
    return Object.assign(defaultOption, option);
}

export const oauthOption = {
    grant_type: process.env.GRANT_TYPE,
    client_id: process.env.CLINET_ID,
    client_secret: process.env.CLIENT_SECRET,
}


export const login = (options) => request(`${BASE_URL}/oauth/token`, getOption(options));