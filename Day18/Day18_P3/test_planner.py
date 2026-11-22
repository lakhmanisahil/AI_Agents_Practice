from agent import create_research_plan


request = (
    "Research about the jobs requirement in robotics engineer domain at Skild ai."
)


plan = create_research_plan(
    request
)


print("\nRESEARCH PLAN\n")
print(plan)

