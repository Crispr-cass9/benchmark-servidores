export interface benchmark_data {
    "Orden Peticion": number;
    "Complete requests": number;
    "Concurrency Level": number;
    Connect: number[];
    "Connection Times (ms)": string;
    "Document Length": string;
    "Document Path": string;
    "Failed requests": number;
    "HTML transferred": string;
    Processing: number[];
    "Requests per second": string;
    "SSL/TLS Protocol": string;
    "Server Hostname": string;
    "Server Port": number;
    "Server Software": string;
    "Server Temp Key": string;
    "TLS Server Name": string;
    "Time per request": string;
    "Time taken for tests": string;
    Total: number[];
    "Total transferred": string;
    "Transfer rate": string;
    Waiting: number[];
    "min mean[+/-sd] median max": string;
  }
  