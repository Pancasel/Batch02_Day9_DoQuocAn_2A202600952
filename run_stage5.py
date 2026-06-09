import subprocess
import time
import sys

print("Starting services...")
registry = subprocess.Popen(["uv", "run", "python", "-m", "registry"])
time.sleep(2)
tax = subprocess.Popen(["uv", "run", "python", "-m", "tax_agent"])
comp = subprocess.Popen(["uv", "run", "python", "-m", "compliance_agent"])
time.sleep(3)
law = subprocess.Popen(["uv", "run", "python", "-m", "law_agent"])
time.sleep(3)
cust = subprocess.Popen(["uv", "run", "python", "-m", "customer_agent"])
time.sleep(5)

print("Running test client...")
subprocess.run(["uv", "run", "python", "test_client.py"])

print("Stopping services...")
for p in [registry, tax, comp, law, cust]:
    p.terminate()
    p.wait()

print("Done!")
