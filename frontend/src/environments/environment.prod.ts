export const environment = {
  production: true,
  apiBaseUrl: (globalThis as any).API_BASE_URL || 'https://<prod-backend-url>'
};
