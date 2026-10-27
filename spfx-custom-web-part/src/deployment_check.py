from dataclasses import dataclass


@dataclass(frozen=True)
class DeploymentCheck:
    package_deployed: bool
    rendered: bool
    data_source_documented: bool
    permission_boundary_documented: bool

    def verify(self) -> str:
        if not self.package_deployed:
            return "NOT VERIFIED: package deployment"
        if not self.rendered:
            return "NOT VERIFIED: runtime rendering"
        if not self.data_source_documented:
            return "NOT VERIFIED: data boundary"
        if not self.permission_boundary_documented:
            return "NOT VERIFIED: permission boundary"
        return "VERIFIED: Northstar Status"


if __name__ == "__main__":
    check = DeploymentCheck(
        package_deployed=True,
        rendered=True,
        data_source_documented=True,
        permission_boundary_documented=True,
    )
    print(check.verify())
