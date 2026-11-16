"use strict";
const $ = (id) => document.getElementById(id);
const state = {
  view: "overview",
  hours: 24,
  node: "",
  metric: "temperature",
  page: 0,
  custom: null,
  data: null,
  error: false,
  sequence: 0,
};
const chile = new Intl.DateTimeFormat("es-CL", {
  timeZone: "America/Santiago",
  day: "2-digit",
  month: "short",
  hour: "2-digit",
  minute: "2-digit",
  hourCycle: "h23",
});
const clock = new Intl.DateTimeFormat("es-CL", {
  timeZone: "America/Santiago",
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
  hourCycle: "h23",
});
const shortClock = new Intl.DateTimeFormat("es-CL", {
  timeZone: "America/Santiago",
  hour: "2-digit",
  minute: "2-digit",
  hourCycle: "h23",
});
const numeric = (value, decimals = 1) =>
  Number.isFinite(value)
    ? value.toLocaleString("es-CL", {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
      })
    : "—";
const date = (value) => (value ? chile.format(new Date(value)) : "—");
const age = (value) =>
  value === null || !Number.isFinite(value)
    ? "Sin datos"
    : value < 60
      ? `${Math.floor(value)} s`
      : value < 3600
        ? `${Math.floor(value / 60)} min`
        : value < 86400
          ? `${Math.floor(value / 3600)} h`
          : `${Math.floor(value / 86400)} días`;
let toastTimeout;
function toast(message) {
  $("toast").textContent = message;
  $("toast").hidden = false;
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => ($("toast").hidden = true), 4500);
}
function query() {
  const p = new URLSearchParams(state.custom || { hours: state.hours });
  if (state.node) p.set("node", state.node);
  return p.toString();
}
function setView(view) {
  state.view = view;
  state.page = 0;
  const title = {
    overview: [
      "Un vistazo al entorno.",
      "Condiciones del nodo y alertas, en un solo lugar.",
      "Vista general",
    ],
    history: [
      "Cada lectura cuenta.",
      "Explora el histórico y observa cómo cambia el entorno.",
      "Histórico",
    ],
    alerts: [
      "Una señal para actuar.",
      "Revisa los eventos SOS registrados por la estación.",
      "Alertas SOS",
    ],
  }[view];
  $("page-title").textContent = title[0];
  $("page-subtitle").textContent = title[1];
  $("breadcrumb-current").textContent = title[2];
  document.querySelectorAll("[data-view]").forEach((b) => {
    const active = b.dataset.view === view;
    b.classList.toggle("active", active);
    if (active) b.setAttribute("aria-current", "page");
    else b.removeAttribute("aria-current");
  });
  $("overview-view").hidden = view !== "overview";
  $("chart-section").hidden = view === "alerts";
  $("readings-section").hidden = view === "alerts";
  $("history-filters").hidden = view !== "history";
  $("alerts-section").hidden = view !== "alerts";
  $("pagination").hidden = view !== "history";
  $("show-history").hidden = view === "history";
  document.querySelector(".range-control").hidden = view === "alerts";
  $("readings-title").textContent =
    view === "history" ? "Histórico de lecturas" : "Últimas lecturas";
  if (state.data) render(state.data);
}
function renderFreshness(data) {
  if (!data) return;
  const received = data.latest
    ? new Date(data.latest.received_at).getTime()
    : null;
  const seconds =
    received === null ? null : Math.max(0, (Date.now() - received) / 1000);
  const stale =
    seconds === null || seconds > data.freshness.stale_after_seconds;
  $("data-age").textContent = age(seconds);
  $("freshness-context").textContent =
    seconds === null
      ? "Aún no se reciben mediciones"
      : stale
        ? "Dato antiguo · revisar nodo y enlace"
        : `Dato reciente · solicitud cada ${data.expected_interval_seconds} s`;
  $("freshness-context").style.color = stale ? "#a17b3c" : "";
  const station = data.station;
  const connected =
    station &&
    station.state === "connected" &&
    Date.now() - new Date(station.updated_at).getTime() <= 15000;
  const pill = $("usb-status");
  pill.className =
    "status-pill " +
    (state.error
      ? "offline"
      : connected
        ? ""
        : station
          ? "offline"
          : "neutral");
  const label = state.error
    ? "Sin actualización del dashboard"
    : connected
      ? "Estación USB conectada"
      : station?.state === "connecting"
        ? "Conectando estación USB"
        : station
          ? "Estación USB sin conexión"
          : "Estado USB no disponible";
  pill.lastChild.textContent = label;
  const alertCount = data.alert_counts.unreviewed;
  let title, body;
  if (alertCount) {
    title = `${alertCount} ${alertCount === 1 ? "alerta SOS requiere" : "alertas SOS requieren"} revisión`;
    body =
      "Abre el registro, verifica el evento y coordina la atención según el procedimiento del proyecto.";
  } else if (stale) {
    title =
      seconds === null
        ? "Esperando datos del entorno"
        : "La última lectura dejó de ser reciente";
    body = `Comprueba la alimentación y el enlace del nodo. El aviso se activa tras ${data.freshness.stale_after_seconds / 60} minutos sin una lectura.`;
  } else if (!connected) {
    title = "La estación necesita revisión";
    body =
      "Los datos guardados siguen disponibles. Revisa el servicio de recepción y la conexión USB para continuar capturando.";
  } else {
    title = "Datos recientes para seguir el entorno";
    const d = data.statistics.delta;
    body = Number.isFinite(d)
      ? `La temperatura ${d >= 0 ? "subió" : "bajó"} ${numeric(Math.abs(d))} °C en el período. Contrasta la tendencia con las condiciones locales antes de planificar una actividad.`
      : "Consulta el histórico para interpretar las condiciones del nodo y detectar cambios.";
  }
  $("decision-title").textContent = title;
  $("decision-body").textContent = body;
  $("decision-banner").classList.toggle(
    "attention",
    Boolean(alertCount) || stale || !connected,
  );
}
function render(data) {
  state.data = data;
  $("temperature").textContent = numeric(data.latest?.temperature);
  $("humidity").textContent = numeric(data.latest?.humidity);
  $("temperature-context").textContent = data.latest
    ? `Recibido ${date(data.latest.received_at)}`
    : "Esperando primera lectura";
  const count = data.alert_counts.unreviewed;
  $("open-alerts").textContent = count;
  $("alert-unit").textContent = count === 1 ? "alerta" : "alertas";
  $("nav-alert-count").textContent = count;
  document.querySelector(".sos-card").classList.toggle("has-alerts", count > 0);
  const stat = data.statistics;
  for (const key of ["mean", "min", "max"])
    $("stat-" + key).textContent = Number.isFinite(stat[key])
      ? `${numeric(stat[key])} °C`
      : "—";
  $("stat-delta").textContent = Number.isFinite(stat.delta)
    ? `${stat.delta > 0 ? "+" : ""}${numeric(stat.delta)} °C`
    : "—";
  $("stat-interval").textContent = Number.isFinite(stat.median_interval_seconds)
    ? `${numeric(stat.median_interval_seconds, 0)} s`
    : "—";
  $("last-refresh").textContent =
    `Actualizado ${clock.format(new Date(data.generated_at))}`;
  $("export-link").href = "/api/export.csv?" + query();
  $("system-detail").textContent =
    `Lecturas solicitadas cada ${data.expected_interval_seconds} s · Pantalla cada 5 s`;
  renderFreshness(data);
  renderChart(data);
  renderReadings(data);
  renderAlerts(data);
}
function renderChart(data) {
  const humidity = state.metric === "humidity",
    unit = humidity ? "%" : "°C",
    name = humidity ? "Humedad relativa" : "Temperatura";
  $("chart-title").textContent = name + " en el tiempo";
  $("chart-legend").textContent = name + " · " + unit;
  const rows = data.readings.filter((r) => Number.isFinite(r[state.metric]));
  const available = rows.length
    ? `${date(rows[0].received_at)} — ${date(rows.at(-1).received_at)}`
    : "Lecturas reales del nodo seleccionado";
  $("chart-subtitle").textContent = available;
  $("chart-point-count").textContent =
    `${rows.length.toLocaleString("es-CL")} muestras${data.truncated ? " · vista limitada" : ""} · Hora de Chile`;
  const svg = $("chart");
  $("chart-empty").hidden = rows.length > 0;
  $("chart-tooltip").hidden = true;
  svg.setAttribute(
    "aria-label",
    `${name}, ${rows.length} muestras reales en ${unit}`,
  );
  if (!rows.length) {
    svg.replaceChildren();
    return;
  }
  const W = Math.max(300, svg.clientWidth || 1100),
    H = W < 600 ? 230 : 265,
    L = 50,
    R = 20,
    T = 16,
    B = 39;
  svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  const vals = rows.map((r) => r[state.metric]);
  let low = Math.min(...vals),
    high = Math.max(...vals);
  const margin = Math.max((high - low) * 0.22, 0.5);
  low -= margin;
  high += margin;
  if (humidity) {
    low = Math.max(0, low);
    high = Math.min(100, high);
  }
  if (high === low) high = low + 1;
  let t0 = new Date(rows[0].received_at).getTime(),
    t1 = new Date(rows.at(-1).received_at).getTime();
  if (t0 === t1) {
    t0 -= 60000;
    t1 += 60000;
  }
  const x = (r) =>
      L + ((new Date(r.received_at).getTime() - t0) / (t1 - t0)) * (W - L - R),
    y = (v) => H - B - ((v - low) / (high - low)) * (H - T - B);
  let markup = `<defs><linearGradient id="area-fill" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stop-color="#dbe9cf" stop-opacity=".65"/><stop offset="100%" stop-color="#edf4e6" stop-opacity=".15"/></linearGradient></defs>`;
  for (let i = 0; i <= 4; i++) {
    const value = low + ((high - low) * i) / 4,
      py = y(value);
    markup += `<line class="chart-grid" x1="${L}" x2="${W - R}" y1="${py}" y2="${py}"/><text class="chart-axis" text-anchor="end" x="${L - 13}" y="${py + 4}">${numeric(value)}${i === 4 ? " " + unit : ""}</text>`;
  }
  const ticks = W < 600 ? 3 : 5;
  for (let i = 0; i <= ticks; i++) {
    const px = L + ((W - L - R) * i) / ticks;
    markup += `<text class="chart-axis" text-anchor="middle" x="${px}" y="${H - 10}">${shortClock.format(new Date(t0 + ((t1 - t0) * i) / ticks))}</text>`;
  }
  const step = Math.max(1, Math.ceil(rows.length / 500));
  const plot = rows.filter((_, i) => i % step === 0 || i === rows.length - 1);
  let segment = [];
  const segments = [];
  for (const row of plot) {
    if (
      segment.length &&
      new Date(row.received_at) - new Date(segment.at(-1).received_at) >
        data.freshness.stale_after_seconds * 1000 * step
    ) {
      segments.push(segment);
      segment = [];
    }
    segment.push(row);
  }
  if (segment.length) segments.push(segment);
  for (const group of segments) {
    const path = group
      .map(
        (r, i) =>
          `${i ? "L" : "M"}${x(r).toFixed(2)},${y(r[state.metric]).toFixed(2)}`,
      )
      .join(" ");
    markup += `<path d="${path} L${x(group.at(-1))},${H - B} L${x(group[0])},${H - B} Z" fill="url(#area-fill)"/><path class="chart-line" d="${path}"/>`;
  }
  plot.forEach((r, i) => {
    markup += `<circle class="chart-point" data-point="${i}" cx="${x(r)}" cy="${y(r[state.metric])}" r="${plot.length > 150 ? 2 : 3}" tabindex="0" aria-label="${numeric(r[state.metric])} ${unit}, ${date(r.received_at)}"/>`;
  });
  svg.innerHTML = markup;
  svg.querySelectorAll("[data-point]").forEach((point) => {
    const show = () => {
      const r = plot[Number(point.dataset.point)],
        tip = $("chart-tooltip");
      tip.replaceChildren();
      const small = document.createElement("small");
      small.textContent = date(r.received_at);
      tip.append(
        small,
        document.createTextNode(`${numeric(r[state.metric])} ${unit}`),
      );
      tip.hidden = false;
      const wrap = svg.parentElement.getBoundingClientRect();
      const box = point.getBoundingClientRect();
      tip.style.left = `${Math.min(Math.max(5, box.left - wrap.left - 35), wrap.width - tip.offsetWidth - 8)}px`;
      tip.style.top = `${Math.max(0, box.top - wrap.top - 58)}px`;
    };
    point.addEventListener("mouseenter", show);
    point.addEventListener("focus", show);
    point.addEventListener(
      "mouseleave",
      () => ($("chart-tooltip").hidden = true),
    );
    point.addEventListener("blur", () => ($("chart-tooltip").hidden = true));
  });
}
function cell(row, text, className = "") {
  const td = document.createElement("td");
  td.textContent = text;
  if (className) td.className = className;
  row.append(td);
  return td;
}
function renderReadings(data) {
  const rows = [...data.readings].reverse(),
    size = state.view === "history" ? 25 : 5,
    maxPage = Math.max(0, Math.ceil(rows.length / size) - 1);
  state.page = Math.min(state.page, maxPage);
  const body = $("readings-body");
  body.replaceChildren();
  rows.slice(state.page * size, (state.page + 1) * size).forEach((r) => {
    const tr = document.createElement("tr");
    cell(tr, date(r.received_at));
    cell(tr, numeric(r.temperature) + " °C", "strong");
    cell(tr, numeric(r.humidity) + " %");
    cell(tr, Number.isFinite(r.rssi) ? numeric(r.rssi, 0) + " dBm" : "—");
    cell(tr, Number.isFinite(r.snr) ? numeric(r.snr) + " dB" : "—");
    body.append(tr);
  });
  $("readings-empty").hidden = rows.length > 0;
  $("readings-subtitle").textContent = data.truncated
    ? "Vista limitada a 20.000 lecturas. Exporta el rango completo en CSV."
    : `${rows.length} lecturas en el período · hora de recepción`;
  $("page-description").textContent = rows.length
    ? `${state.page * size + 1}–${Math.min((state.page + 1) * size, rows.length)} de ${rows.length}`
    : "Sin lecturas";
  $("previous-page").disabled = state.page === 0;
  $("next-page").disabled = state.page >= maxPage;
}
function badge(text, className = "") {
  const span = document.createElement("span");
  span.className = "tag " + className;
  span.textContent = text;
  return span;
}
function renderAlerts(data) {
  const body = $("alerts-body");
  body.replaceChildren();
  $("alerts-empty").hidden = data.alerts.length > 0;
  data.alerts.forEach((alert) => {
    const row = document.createElement("tr");
    cell(row, date(alert.first_received_at));
    const event = cell(row, alert.event_id.slice(-8), "alert-event");
    event.title = alert.event_id;
    const ack = cell(row, "");
    ack.append(
      badge(
        alert.ack_state === "queued"
          ? "ACK encolado"
          : alert.ack_state === "pending"
            ? "ACK pendiente"
            : "Sin información",
        alert.ack_state === "pending" ? "pending" : "neutral",
      ),
    );
    if (alert.last_error) ack.title = alert.last_error;
    const review = cell(row, "");
    review.append(
      badge(
        alert.reviewed_at ? "Revisada" : "Por revisar",
        alert.reviewed_at ? "neutral" : "pending",
      ),
    );
    if (alert.reviewed_at) {
      const small = document.createElement("small");
      small.className = "review-time";
      small.textContent = date(alert.reviewed_at);
      review.append(small);
    }
    const action = cell(row, "");
    const button = document.createElement("button");
    button.className = "button secondary";
    button.textContent = alert.reviewed_at ? "Reabrir" : "Marcar revisada";
    button.addEventListener("click", async () => {
      button.disabled = true;
      try {
        const response = await fetch("/api/alerts/review", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            node: alert.node,
            event_id: alert.event_id,
            reviewed: !alert.reviewed_at,
          }),
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.error);
        toast(alert.reviewed_at ? "Alerta reabierta" : "Revisión guardada");
        await load();
      } catch (error) {
        toast(error.message);
        button.disabled = false;
      }
    });
    action.append(button);
    body.append(row);
  });
}
async function load() {
  const sequence = ++state.sequence;
  try {
    const response = await fetch("/api/dashboard?" + query(), {
      cache: "no-store",
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error);
    if (sequence !== state.sequence) return;
    if (!state.node && data.nodes.length) {
      state.node = data.nodes[0].id;
      return load();
    }
    const select = $("node-select");
    const ids = Array.from(select.options)
      .map((o) => o.value)
      .join(",");
    if (ids !== data.nodes.map((n) => n.id).join(",")) {
      select.replaceChildren();
      if (!data.nodes.length) {
        const o = new Option("Sin nodos recibidos", "");
        select.add(o);
      }
      data.nodes.forEach((n) => select.add(new Option("RAK · " + n.id, n.id)));
    }
    select.value = state.node;
    select.disabled = data.nodes.length < 2;
    state.error = false;
    $("api-error").hidden = true;
    render(data);
  } catch (error) {
    if (sequence !== state.sequence) return;
    state.error = true;
    $("api-error").textContent =
      "No se pudo actualizar el dashboard. " + error.message;
    $("api-error").hidden = false;
    renderFreshness(state.data);
  }
}
document
  .querySelectorAll("[data-view]")
  .forEach((b) => b.addEventListener("click", () => setView(b.dataset.view)));
$("review-alerts").addEventListener("click", () => setView("alerts"));
$("show-history").addEventListener("click", () => setView("history"));
$("node-select").addEventListener("change", (e) => {
  state.node = e.target.value;
  state.page = 0;
  load();
});
document.querySelectorAll("[data-hours]").forEach((b) =>
  b.addEventListener("click", () => {
    state.hours = Number(b.dataset.hours);
    state.custom = null;
    state.page = 0;
    document.querySelectorAll("[data-hours]").forEach((x) => {
      x.classList.toggle("selected", x === b);
      x.setAttribute("aria-pressed", String(x === b));
    });
    load();
  }),
);
document.querySelectorAll("[data-metric]").forEach((b) =>
  b.addEventListener("click", () => {
    state.metric = b.dataset.metric;
    document.querySelectorAll("[data-metric]").forEach((x) => {
      x.classList.toggle("selected", x === b);
      x.setAttribute("aria-pressed", String(x === b));
    });
    if (state.data) renderChart(state.data);
  }),
);
$("previous-page").addEventListener("click", () => {
  state.page--;
  renderReadings(state.data);
});
$("next-page").addEventListener("click", () => {
  state.page++;
  renderReadings(state.data);
});
$("date-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const start = new Date($("date-from").value),
    end = new Date($("date-until").value);
  if (
    !Number.isFinite(start.getTime()) ||
    !Number.isFinite(end.getTime()) ||
    start > end
  ) {
    toast("Selecciona un rango de fechas válido");
    return;
  }
  state.custom = { since: start.toISOString(), until: end.toISOString() };
  state.page = 0;
  document.querySelectorAll("[data-hours]").forEach((b) => {
    b.classList.remove("selected");
    b.setAttribute("aria-pressed", "false");
  });
  load();
});
$("date-clear").addEventListener("click", () =>
  document.querySelector('[data-hours="24"]').click(),
);
load();
setInterval(load, 5000);
setInterval(() => renderFreshness(state.data), 1000);
