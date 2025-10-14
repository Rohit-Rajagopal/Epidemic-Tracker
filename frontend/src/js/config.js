const backend_endpoint = "https://optionally-resolved-cicada.ngrok-free.app/";

const locations_route = "locations/entries_by_location";

const clusters_route = "clusters";

const add_news_route = "user-report";

const locations_url = backend_endpoint + locations_route;

const clusters_url = backend_endpoint + clusters_route;

const add_news_url = backend_endpoint + add_news_route;


export { locations_url, clusters_url, backend_endpoint, add_news_url };