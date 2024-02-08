def pytest_collection_finish(session):
    quick_tests_count = 0
    long_tests_count = 0

    for item in session.items:
        if 'long_running' in item.keywords:
            long_tests_count += 1
        else:
            quick_tests_count += 1

    print(f"Collected quick tests: {quick_tests_count}, long-running tests: {long_tests_count}")
