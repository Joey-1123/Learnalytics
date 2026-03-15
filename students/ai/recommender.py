class SubjectRecommender:

    PASS_MARK = 40

    @classmethod
    def weak_subjects(cls, marks):
        """
        Return subjects where score is below pass mark
        """

        weak = []

        for mark in marks:
            if mark.score < cls.PASS_MARK:
                weak.append(mark.subject)

        return weak


    @classmethod
    def study_recommendations(cls, weak_subjects):
        """
        Generate study suggestions
        """

        recommendations = []

        for subject in weak_subjects:
            recommendations.append(
                f"Spend more practice time on {subject}"
            )

        return recommendations