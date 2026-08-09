import logging

from mdm_merge_recommendation_engine.config import load_config


def main():
    config = load_config()

    logging.basicConfig(level=config.log_level)
    logger = logging.getLogger(__name__)

    logger.info(f"Starting MDM Merge Recommendation Engine")
    logger.info(f"Environment: {config.environment}")
    logger.info(f"Cluster: {config.cluster_id}")
    logger.info(f"Workspace: {config.workspace_url}")


if __name__ == "__main__":
    main()
