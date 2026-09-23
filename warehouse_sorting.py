
def check_package(package_id):
    """
    Function to evaluate package ID status.
    Returns:
        "low" for low-priority
        "high" for high-risk
        "process" for valid processing
        "invalid" for invalid ID (0 or negative)
    """
    if package_id <= 0:
        return "invalid"
    elif package_id < 1000:
        return "low"
    elif package_id > 9000:
        return "high"
    else:
        return "process"


# Original queue of incoming package IDs
package_queue = [984, 1520, 2983, 0, 9912, 4871, 102, 3100]

# Shallow copy of the original queue
copy_queue = package_queue[:]

processed_packages = []

# Process packages
for package in package_queue:
    status = check_package(package)

    if status == "invalid":
        print(f"Package ID {package} is invalid. Skipping.")
        continue

    if status == "low":
        print(f"Package {package} is low-priority. Skipping.")
        continue

    if status == "high":
        print(f"Package {package} is high-risk! Halting process.")
        break

    if status == "process":
        print(f"Package {package} is processed.")
        processed_packages.append(package)

print("\nFinal Processed Packages:\n")
print(processed_packages)

print("\nOriginal Queue (before change):\n")
print(package_queue)

# Modify the original queue to demonstrate shallow copy behavior
package_queue[1] = 8888

print("\nModified Original Queue:\n")
print(package_queue)

print("\nCopy Queue (should not change):\n")
print(copy_queue)