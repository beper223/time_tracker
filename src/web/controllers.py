from flask import jsonify, request
from http import HTTPStatus

from src.services.work_time import WorkTimeService

class TaskController:

    def __init__(self):
        self.work_time_service = WorkTimeService()

    def get_tasks(self):
        result = self.work_time_service.get_work_times()

        return jsonify({
            'status': 'success',
            'data': result,
            'count': len(result)
        }), HTTPStatus.OK

    def new_task(self):
        if request.method == 'POST':
            task = Task(
                description=request.form['description'],
                task_type=TaskType[request.form['task_type']],
                work_date=datetime.strptime(request.form['work_date'], "%Y-%m-%d").date(),
                start_time=datetime.strptime(request.form['start_time'], "%H:%M").time() if request.form[
                    'start_time'] else None,
                end_time=datetime.strptime(request.form['end_time'], "%H:%M").time() if request.form[
                    'end_time'] else None,
                is_closed='is_closed' in request.form
            )
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('task.index'))

        return render_template('task/edit.html', task=None, task_types=TaskType)