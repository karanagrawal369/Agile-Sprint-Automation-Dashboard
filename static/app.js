document.addEventListener("DOMContentLoaded", function(){
  const runSprintBtn = document.getElementById("runSprint");
  const runTriageBtn = document.getElementById("runTriage");
  const runQABtn = document.getElementById("runQA");
  const refreshBtn = document.getElementById("refresh");
  const traceEl = document.getElementById("trace");
  const sessionEl = document.getElementById("session");
  const loader = document.getElementById("loader");

  function showLoader(on){
    loader.style.display = on ? "block" : "none";
  }

  async function apiCall(path, method="POST"){
    showLoader(true);
    try{
      const res = await fetch(path, { method });
      if(!res.ok){
        const text = await res.text();
        throw new Error(res.status + " " + text);
      }
      return await res.json();
    } finally {
      showLoader(false);
    }
  }

  async function refresh(){
    showLoader(true);
    try{
      const res = await fetch("/status");
      if(!res.ok) throw new Error("status fetch failed");
      const json = await res.json();
      traceEl.textContent = JSON.stringify(json.trace || [], null, 2);
      sessionEl.textContent = JSON.stringify(json.last_session || {}, null, 2);
    } catch(e){
      traceEl.textContent = "Error loading status: " + e.message;
      sessionEl.textContent = "{}";
    } finally {
      showLoader(false);
    }
  }

  runSprintBtn.addEventListener("click", async function(){
    await apiCall("/run/sprint-cycle","POST");
    await refresh();
  });

  runTriageBtn.addEventListener("click", async function(){
    await apiCall("/agents/triage/run","POST");
    await refresh();
  });

  runQABtn.addEventListener("click", async function(){
    const sprintId = prompt("Enter sprint id", "s1") || "s1";
    await apiCall(`/agents/qa/generate?sprint_id=${encodeURIComponent(sprintId)}`,"POST");
    await refresh();
  });

  refreshBtn.addEventListener("click", refresh);

  refresh();
});
