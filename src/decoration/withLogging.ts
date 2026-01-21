function withLogging<T extends (...args: any[]) => any>(fn: T): T {
  return ((...args: any[]) => {
    console.log(`[LOG] ${fn.name} chaqirildi →`, args);
    return fn(...args);
  }) as T;
}
