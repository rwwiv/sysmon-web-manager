export class ApiConstants {
    public static API_URL = (process.env.VUE_APP_API_URL == undefined) ? window.location.hostname : process.env.VUE_APP_API_URL;
    public static API_PORT = (process.env.VUE_APP_API_PORT == undefined) ? 8000 : process.env.VUE_APP_API_PORT;
    public static API_FULL_ENDPOINT = `${ApiConstants.API_URL}:${ApiConstants.API_PORT}`
}
