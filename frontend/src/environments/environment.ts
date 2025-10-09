export const environment = {
  production: false,
  apiBaseUrl: (globalThis as any).API_BASE_URL || 'http://localhost:8080'
};
